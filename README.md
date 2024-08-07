# illumioAssesment-HarshPatni


1. The flow log data file is in CSV format and has the destination port and protocol in the 4th and 5th columns respectively.
2. The lookup table file is in CSV format and has the destination port, protocol, and tag in the 1st, 2nd, and 3rd columns respectively.
3. The output file is a plain text file with tab-separated values.
4. The matches are case insensitive.
5. If a row in the flow log data does not match any entry in the lookup table, it is tagged as 'Untagged'.
6. The flow log file size can be up to 10 MB.
7. The lookup file can have up to 10,000 mappings.
8. The tags can map to more than one port, protocol combinations.