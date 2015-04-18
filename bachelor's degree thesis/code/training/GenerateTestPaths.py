from FindAllPaths import *

timeSpan = "1970_1985"
timeSpanEnd = 1985
nodesDict = InitialData.InitialNodesPairWeightDict(timeSpan)
communities = CommunityDetectionByUsingLouvain.ReadCommunitiesFromFile(timeSpan)
print "Read"

for nodes in communities:

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
		#if IsNodeActiveRecently(nodes[i], activeYearsDict, 1979):
		pathsDict = {}
		for j in xrange(0, len(nodes)):
			if i != j and nodes[j] not in communityNodesDict[nodes[i]]:# and IsNodeActiveRecently(nodes[j], activeYearsDict, 1979) and IfActiveYearsOverlap(nodes[i], nodes[j], activeYearsDict):
				paths = list(nx.all_simple_paths(G, source = nodes[i], target = nodes[j], cutoff = 6))
				if len(paths) != 0:
					pathsDict[nodes[j]] = paths
		pathsDictFile = open("./temp data/PathsDict" + timeSpan + "/" + str(nodes[i]), "w")
		pickle.dump(pathsDict, pathsDictFile)
		pathsDictFile.close()


