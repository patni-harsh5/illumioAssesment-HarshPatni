import csv
import random

# Load the lookup table
lookup_table = []
pathLookupTable = 'lookup_table.csv'
with open(pathLookupTable, 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header
    for row in reader:
        dstport, protocol = row[:2]
        lookup_table.append((dstport, protocol))

# Generate the flow log file
pathFlowLog = 'flow_log.txt'
with open(pathFlowLog, 'w') as f:
    for _ in range(1000):  # Change this to the number of lines you want
        dstport, protocol = random.choice(lookup_table)
        # Assume the other fields are 'field1', 'field2', etc.
        f.write(f'field1 field2 field3 {dstport} {protocol} field6 field7 field8\n')