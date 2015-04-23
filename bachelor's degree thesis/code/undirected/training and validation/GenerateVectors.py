from FindAllPaths import *
import CommunityDetectionByUsingLouvain
import GenerateVector

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
			for j in xrange(i + 1, len(nodes)):
				if nodes[j] not in communityNodesDict[nodes[i]]:
					paths = list(nx.all_simple_paths(G, source = nodes[i], target = nodes[j], cutoff = 6))
					if len(paths) != 0:
						vector = GenerateVector.GenerateVector(paths, nodesDict)
						if nodes[i] not in vectorsDict:
							vectorsDict[nodes[i]] = {}
						if nodes[j] not in vectorsDict:
							vectorsDict[nodes[j]] = {}
						vectorsDict[nodes[i]][nodes[j]] = vector
						vectorsDict[nodes[j]][nodes[i]] = vector
			print("nodes[%s] generated"%nodes[i])

	vectorsDictFile = open("./temp data/Vectors" + timeSpan, "w")
	pickle.dump(vectorsDict, vectorsDictFile)
	vectorsDictFile.close()
	print("timeSpan%s generated"%timeSpan)

if __name__ == '__main__':
	GenerateVectors("2004_2006")
	GenerateVectors("2004_2007")