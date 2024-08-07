import csv
from collections import Counter

# Load the lookup-table
lookup_table = {}
pathLookupTable = 'lookup_table.csv'
with open(pathLookupTable, 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header
    for row in reader:
        dstport, protocol, tag = row
        lookup_table[(dstport.lower(), protocol.lower())] = tag.lower()

# Initialize the Counters
tag_counts = Counter()
port_protocol_counts = Counter()

pathFlowLog = 'flow_log.txt'
# Parse the flow log file
with open(pathFlowLog, 'r') as f:
    for line in f:
        # Assume the dstport and protocol are the 4th and 5th fields in the line
        fields = line.split()
        dstport, protocol = fields[3].lower(), fields[4].lower()

        # Look up the tag
        tag = lookup_table.get((dstport, protocol), 'untagged')

        # Increment the counts
        tag_counts[tag] += 1
        port_protocol_counts[(dstport, protocol)] += 1

pathOutput = 'output.txt'
# Write the counts to the output-file
with open(pathOutput, 'w') as f:
    f.write('Tag Counts:\n')
    for tag, count in tag_counts.items():
        f.write(f'{tag}\t{count}\n')

    f.write('\nPort/Protocol Combination Counts:\n')
    for (dstport, protocol), count in port_protocol_counts.items():
        f.write(f'{dstport}\t{protocol}\t{count}\n')