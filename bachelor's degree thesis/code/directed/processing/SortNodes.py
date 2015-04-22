#Author: Kai Huang
#Date: 2015.04.20

import sys
sys.path.append("../tools")
import DateConversion
import StringProcessing
import DataInfo
#read
lines = open("../../../data/enron/out.enron", "r")
lines.readline() #ignore the first line
nodes = [None] * (DataInfo.NodesCount + 1)
for i in xrange(0, len(nodes)):
	nodes[i] = []
for line in lines:
	tokens = StringProcessing.SplitLine(line)
	newLine = "".join([tokens[0], ' ', tokens[1], ' ', tokens[2], ' ', tokens[3], ' ', DateConversion.SecsToDatetime(int(tokens[3])), '\n'])
	nodes[int(tokens[0])].append(newLine)
lines.close()
#write
sortedLines = open("../../../data/enron/sorted_out.enron", "w")
for i in nodes:
	for j in i:
		sortedLines.write(j)
sortedLines.close()