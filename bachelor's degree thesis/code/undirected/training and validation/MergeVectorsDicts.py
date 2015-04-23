
import InitialData
import pickle

# ###merge 9####
# #filesNames, fullFilesNames = InitialData.FileWalker("./temp data/Vectors1970_1985/9")
# vectorsDict = {}
# for fullFileName in fullFilesNames:
# 	vectorDictFile = open(fullFileName)
# 	vectorDict = pickle.load(vectorDictFile)
# 	for i in vectorDict:
# 		if i not in vectorsDict:
# 			vectorsDict[i] = {}
# 		vectorsDict[i].update(vectorDict[i])
# vectorsDictFile = open("./temp data/Vectors1970_1985/Vectors_9", "w")
# pickle.dump(vectorsDict, vectorsDictFile)

vectorsDict = {}
filesNames, fullFilesNames = InitialData.FileWalker("./temp data/Vectors1970_1985_bak")
for fullFileName in fullFilesNames:
	print fullFileName
	vectorDictFile = open(fullFileName)
	vectorsDict.update(pickle.load(vectorDictFile))

vectorsDictFile = open("./temp data/Vectors1970_1985", "w")
pickle.dump(vectorsDict, vectorsDictFile)
