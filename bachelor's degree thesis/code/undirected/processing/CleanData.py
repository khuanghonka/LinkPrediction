#Author: Kai Huang
#Date: 2015.04.01

import sys
sys.path.append("../tools")
import DateConversion
import StringProcessing
def CleanData():
	#read
	lines = open("../../../data/dblp/dblp.data", "r")
	nodes = {}
	for line in lines:
		tokens = StringProcessing.SplitLine(line)
		if tokens[0] != tokens[1]:# and int(tokens[0]) in nodesList and int(tokens[1]) in nodesList:
			if int(tokens[0]) not in nodes:
				nodes[int(tokens[0])] = []
			newLine = "".join([tokens[0], ' ', tokens[1], ' ', tokens[2], ' ', tokens[3], ' ', DateConversion.SecsToYear(int(tokens[3])), '\n'])
			nodes[int(tokens[0])].append(newLine)
		
	lines.close()
	#write
	sortedLines = open("../../../data/dblp/cleaned_dblp.data", "w")
	for i in nodes:
		for j in nodes[i]:
			sortedLines.write(j)
	sortedLines.close()

if __name__ == '__main__':
	CleanData()