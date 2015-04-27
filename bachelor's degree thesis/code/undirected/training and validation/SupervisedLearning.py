# Author: Kai Huang
# Date: 2015.4.21

from svmutil import *
import InitialData
import pickle

class SupervisedLearning:
	def GenerateSVMModel(self, firstTimeSpan, secondTimeSpan):
		y, x = self.GenerateYAndX(firstTimeSpan, secondTimeSpan)
		prob  = svm_problem(y, x)
		param = svm_parameter('-t 2 -c 4 -v 4')
		self.m = svm_train(prob, param)
		#svm_save_model("./temp data/Model1970_1979", self.m)

	def Validate(self, firstTimeSpan, secondTimeSpan):
		#self.m = svm_load_model("./temp data/Model1970_1979") 
		y, x = self.GenerateYAndX(firstTimeSpan, secondTimeSpan)
		p_label, p_acc, p_val = svm_predict(y, x, self.m)
		nodesDict = InitialData.InitialNodesPairWeightDict(secondTimeSpan)
		print "len(nodesDict) = ", len(nodesDict)
		nodesList = InitialData.InitialNodesList(firstTimeSpan)
		print "len(nodesList) = ", len(nodesList)
		linksAppeared = 0
		for i in nodesDict:
			if i in nodesList:
				for j in nodesDict[i]:
					if j in nodesList:
						linksAppeared += 1
		truePositive = 0
		falsePositve = 0

		print "linksAppeared = ", linksAppeared

		yfile = open("./temp data/y", "w")
		for i in y:
			yfile.write(str(i) + "\n")

		wfile = open("./temp data/p_label", "w")
		for i in p_label:
			wfile.write(str(i) + "\n")

		for i in xrange(0, len(p_label)):
			if p_label[i] == 1:
				if y[i] == 1:
					truePositive += 1
				else:
					falsePositve += 1

		print "truePositive = ", truePositive, "falsePositve = ", falsePositve

		precision = float(truePositive) / (truePositive + falsePositve)
		recall = float(truePositive) / linksAppeared
		print "precision = ", precision, "recall = ", recall


	def GenerateYAndX(self, firstTimeSpan, secondTimeSpan):
		nodesDict = InitialData.InitialNodesPairWeightDict(secondTimeSpan)
		vectorsDictFile = open("./temp data/Vectors" + firstTimeSpan)
		vectorsDict = pickle.load(vectorsDictFile)
		y = []#y: a Python list/tuple of l labels (type must be int/double).
		x = []#x: a Python list/tuple of l data instances. Each element of x must be an instance of list/tuple/dictionary type.
		for i in vectorsDict:
			for j in vectorsDict[i]:
				x.append(vectorsDict[i][j])
				print("i: %s, j: %s"%(i, j))
				if i in nodesDict and j in nodesDict[i]:
					y.append(1)
				else:
					y.append(-1)
		return y, x

supervisedLearning = SupervisedLearning()
supervisedLearning.GenerateSVMModel("2004_2005", "2006")
supervisedLearning.GenerateSVMModel("2004_2006", "2007")