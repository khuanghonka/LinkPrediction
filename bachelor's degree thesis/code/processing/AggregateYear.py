#Author: Kai Huang
#Date: 2015.04.02

import sys
sys.path.append("../tools")
import StringProcessing
lines = open("../../data/dblp_coauthor/sorted_out.dblp_coauthor", "r")
counts = {}
for line in lines:
	tokens = StringProcessing.SplitLine(line)
	counts[tokens[4]] = counts.get(tokens[4], 0) + 1
lines.close()
result = open("../../data/dblp_coauthor/aggregate.dblp_coauthor", "w")
for key in sorted(counts.keys()):
	result.write(key + ' ' + str(counts[key]) + '\n')
result.close()