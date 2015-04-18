#Author: Kai Huang
#Date: 2015.04.07

import sys
sys.path.append("../tools")
import DataInfo
import pickle
import InitialData
import CalSubgraphAddress
import hashlib
import os

def CompleteGroup(path, nodesDict):
	pathDict = {}
	for i in path:
		for j in path:
			if j in nodesDict[i]:
				if i not in pathDict:
					pathDict[i] = {}
				pathDict[i][j] = 1
	return pathDict
def HashPath(path):
	s = ""
	for i in sorted(path):
		s += str(i) + " "
	return hashlib.md5(s.encode("utf-8")).hexdigest()

def GenerateVectors(pathsDict, nodesDict, node):
	vectors = {}
	for target in pathsDict:
		pathSet = set()
		vector = {}
		for path in pathsDict[target]:
			if HashPath(path) not in pathSet:
				pathSet.add(HashPath(path))
				pathDict = CompleteGroup(path, nodesDict)
				nodeMapping = {node:1, target:2}
				for i in xrange(1, len(path) - 1):
					nodeMapping[path[i]] = i + 2
				adjacencyMatrix = InitialData.InitialMatrix()
				for i in pathDict:
					for j in pathDict[i]:
						adjacencyMatrix[nodeMapping[i]][nodeMapping[j]] = 1
						adjacencyMatrix[nodeMapping[j]][nodeMapping[i]] = 1
				minAddress = CalSubgraphAddress.ArgMinAddress(adjacencyMatrix)
				vector[minAddress] = vector.get(minAddress, 0) + 1
		if node not in vectors:
			vectors[node] = {}
		vectors[node][target] = vector
	return vectors

if __name__ == '__main__':

	timeSpan = "1970_1979"
	filesNames, fullFilesNames = InitialData.FileWalker("./temp data/PathsDict" + timeSpan + "")
	for i in xrange(0, len(fullFilesNames)):
		print filesNames[i]
		print fullFilesNames[i]
		pathsDictFile = open(fullFilesNames[i], "r")
		pathsDict = pickle.load(pathsDictFile)
		pathsDictFile.close()
		nodesDict = InitialData.InitialNodesPairWeightDict(timeSpan)
		vectors = GenerateVectors(pathsDict, nodesDict, filesNames[i])
		vectorsFile = open("./temp data/Vectors" + timeSpan + "/"+ filesNames[i], "w")
		pickle.dump(vectors, vectorsFile)
		vectorsFile.close()