from FindAllPaths import *
import CommunityDetectionByUsingLouvain
import GenerateVector
import time
def GenerateVectors(timeSpan):

	nodesDict = InitialData.InitialNodesPairWeightDict(timeSpan)
	communities = CommunityDetectionByUsingLouvain.ReadCommunitiesFromFile(timeSpan)
	print "Read"

	vectorsDict = {}
	for nodes in communities:
		print("Community size = %d"%len(nodes))
		
		G = nx.Graph()
		communityNodesDict = {}
		for i in nodes:
			if i not in communityNodesDict:
				communityNodesDict[i] = []
			for j in nodesDict[i]:
				if j in nodes:
					communityNodesDict[i].append(j)
					G.add_edge(i, j)

		for i in xrange(0, len(nodes)):
			startTime = time.time()
			for j in xrange(i + 1, len(nodes)):
				if nodes[j] not in communityNodesDict[nodes[i]]:
					# startTime = time.time()
					paths = list(nx.all_simple_paths(G, source = nodes[i], target = nodes[j], cutoff = 6))
					# endTime = time.time()
					# print("find paths time:%f"%(endTime - startTime))
					if len(paths) != 0:
						# startTime = time.time()
						vector = GenerateVector.GenerateVector(paths, nodesDict)
						if nodes[i] not in vectorsDict:
							vectorsDict[nodes[i]] = {}
						if nodes[j] not in vectorsDict:
							vectorsDict[nodes[j]] = {}
						vectorsDict[nodes[i]][nodes[j]] = vector
						vectorsDict[nodes[j]][nodes[i]] = vector
						# endTime = time.time()
						# print("generate vector time:%f"%(endTime - startTime))
			endTime = time.time()
			print("nodes[%s] generated, finished in %f s"%(nodes[i], endTime - startTime))

	vectorsDictFile = open("./temp data/Vectors" + timeSpan, "w")
	pickle.dump(vectorsDict, vectorsDictFile)
	vectorsDictFile.close()
	print("timeSpan%s generated"%timeSpan)

if __name__ == '__main__':
	GenerateVectors("2004_2006")
	GenerateVectors("2004_2007")	