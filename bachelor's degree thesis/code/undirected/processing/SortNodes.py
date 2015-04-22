#Author: Kai Huang
#Date: 2015.04.01

import sys
sys.path.append("../tools")
import DateConversion
import StringProcessing
import DataInfo
#read
lines = open("../../../data/dblp_coauthor/out.dblp_coauthor", "r")
lines.readline() #ignore the first line
nodes = [None] * (DataInfo.NodesCount + 1)
for i in xrange(0, len(nodes)):
	nodes[i] = []
for line in lines:
	tokens = StringProcessing.SplitLine(line)
	newLine = "".join([tokens[0], ' ', tokens[1], ' ', tokens[2], ' ', tokens[3], ' ', DateConversion.SecsToYear(int(tokens[3])), '\n'])
	nodes[int(tokens[0])].append(newLine)
lines.close()
#write
sortedLines = open("../../../data/dblp_coauthor/sorted_out.dblp_coauthor", "w")
for i in nodes:
	for j in i:
		sortedLines.write(j)
sortedLines.close()