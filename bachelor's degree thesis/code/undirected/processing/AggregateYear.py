#Author: Kai Huang
#Date: 2015.04.02

import sys
sys.path.append("../tools")
import StringProcessing
lines = open("../../../data/dblp/cleaned_dblp.data", "r")
counts = {}
for line in lines:
	tokens = StringProcessing.SplitLine(line)
	counts[tokens[4]] = counts.get(tokens[4], 0) + 1
lines.close()
result = open("../../../data/dblp/aggregate.data", "w")
for key in sorted(counts.keys()):
	result.write(key + ' ' + str(counts[key]) + '\n')
result.close()