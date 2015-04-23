#Author: Kai Huang
#Date: 2015.04.10

import sys
sys.path.append("../tools")
import StringProcessing
import pickle

def CalWeight(timeSpan):
	lines = open("../../../data/facebook-wosn-wall/edges" + timeSpan + ".facebook-wosn-wall", "r")
	nodesPairWeightDict = {}
	for line in lines:
		tokens = StringProcessing.SplitLine(line)
		first = int(tokens[0])
		second = int(tokens[1])
		if first not in nodesPairWeightDict:
			nodesPairWeightDict[first] = {}
		nodesPairWeightDict[first][second] = nodesPairWeightDict[first].get(second, 0) + 1
	nodesPairWeightDictFile = open("../../../data/facebook-wosn-wall/NodesPairWeightDict" + timeSpan+ ".facebook-wosn-wall", "w")
	pickle.dump(nodesPairWeightDict, nodesPairWeightDictFile)
	nodesPairWeightDictFile.close()

if __name__ == '__main__':
	CalWeight("2004_2006")
	CalWeight("2007")
	CalWeight("2004_2007")
	CalWeight("2008")