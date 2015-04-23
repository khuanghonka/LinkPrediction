#Author: Kai Huang
#Date: 2015.04.02

import sys
sys.path.append("../tools")
import StringProcessing
lines = open("../../../data/facebook-wosn-wall/sorted_out.facebook-wosn-wall", "r")
counts = {}
for line in lines:
	tokens = StringProcessing.SplitLine(line)
	counts[tokens[4]] = counts.get(tokens[4], 0) + 1
lines.close()
result = open("../../../data/facebook-wosn-wall/aggregate.facebook-wosn-wall", "w")
for key in sorted(counts.keys()):
	result.write(key + ' ' + str(counts[key]) + '\n')
result.close()