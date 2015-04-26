
import InitialData
import pickle

# # ###merge 9####
# filesNames, fullFilesNames = InitialData.FileWalker("./temp data/8_9/")
# vectorsDict = {}
# for fullFileName in fullFilesNames:
# 	vectorDictFile = open(fullFileName)
# 	vectorDict = pickle.load(vectorDictFile)
# 	for i in vectorDict:
# 		if i not in vectorsDict:
# 			vectorsDict[i] = {}
# 		vectorsDict[i].update(vectorDict[i])
# vectorsDictFile = open("./temp data/Vectors2004_2006_8_9", "w")
# pickle.dump(vectorsDict, vectorsDictFile)

vectorsDict = {}
filesNames, fullFilesNames = InitialData.FileWalker("./temp data/Vectors2004_2006_parts")
for fullFileName in fullFilesNames:
	print fullFileName
	vectorDictFile = open(fullFileName)
	vectorsDict.update(pickle.load(vectorDictFile))

vectorsDictFile = open("./temp data/Vectors2004_2006_part1", "w")
pickle.dump(vectorsDict, vectorsDictFile)
