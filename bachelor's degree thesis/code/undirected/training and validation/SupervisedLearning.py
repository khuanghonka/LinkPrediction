# Author: Kai Huang
# Date: 2015.4.21

import InitialData
import StringProcessing
import pickle
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.svm import SVC
from sklearn import grid_search
from sklearn.metrics import f1_score, recall_score, precision_score, roc_auc_score
import sys
sys.path.append("../tools")
import DataInfo


class SupervisedLearning:
	def __init__(self, firstTrainingStartTime, firstTrainingEndTime, secondTrainingStartTime, secondTrainingEndTime, firstTestingStartTime, firstTestingEndTime, secondTestingStartTime, secondTestingEndTime):
		self.firstTrainingStartTime = firstTrainingStartTime
		self.firstTrainingEndTime = firstTrainingEndTime
		self.secondTrainingStartTime = secondTrainingStartTime
		self.secondTrainingEndTime = secondTrainingEndTime
		self.firstTestingStartTime = firstTestingStartTime
		self.firstTestingEndTime = firstTestingEndTime
		self.secondTestingStartTime = secondTestingStartTime
		self.secondTestingEndTime = secondTestingEndTime

	def GenerateSVMModel(self):
		x, y = self.GenerateXAndYForTraining()
		parameters = {'C':[1, 10]}
		svc = SVC(kernel = 'linear')
		self.clf = grid_search.GridSearchCV(svc, parameters)
		self.clf.fit(x, y)

	def Validate(self):
		print self.clf.get_params()
		x, y_true  = self.GenerateXAndYForTesting()
		y_predict = self.clf.predict(x)
		
		y_score = self.clf.decision_function(x)
		print "roc", roc_auc_score(y_true, y_score)

		print "recall_score", recall_score(y_true, y_predict)
		print "precision_score", precision_score(y_true, y_predict)

	def GenerateXAndYForTraining(self):
		nodesDict = InitialData.InitialNodesPairWeightDict(self.secondTrainingStartTime, self.secondTrainingEndTime)
		firstTimeSpan = StringProcessing.GetTimeSpan(self.firstTrainingStartTime, self.firstTrainingEndTime)
		vectorsDictFile = open("./temp data/Vectors" + firstTimeSpan)
		vectorsDict = pickle.load(vectorsDictFile)
		row = []
		col = []
		data = []
		y = []
		rowId = 0
		self.features = set()
		for i in vectorsDict:
			for j in vectorsDict[i]:
				for k in vectorsDict[i][j]:
					self.features.add(k)
					row.append(rowId)
					col.append(k)
					data.append(vectorsDict[i][j][k])
				if i in nodesDict and j in nodesDict[i]:
					y.append(1)
				else:
					y.append(-1)
				rowId += 1
		x = csr_matrix((data, (row, col)))
		return x, np.array(y)

	def GenerateXAndYForTesting(self):
		nodesDict = InitialData.InitialNodesPairWeightDict(self.secondTestingStartTime, self.secondTestingEndTime)
		firstTimeSpan = StringProcessing.GetTimeSpan(self.firstTestingStartTime, self.firstTestingEndTime)
		vectorsDictFile = open("./temp data/Vectors" + firstTimeSpan)
		vectorsDict = pickle.load(vectorsDictFile)
		row = []
		col = []
		data = []
		y = []
		rowId = 0
		for i in vectorsDict:
			for j in vectorsDict[i]:
				for k in vectorsDict[i][j]:
					if k in self.features:
						row.append(rowId)
						col.append(k)
						data.append(vectorsDict[i][j][k])
				if i in nodesDict and j in nodesDict[i]:
					y.append(1)
				else:
					y.append(-1)
				rowId += 1
		x = csr_matrix((data, (row, col)))
		return x, np.array(y)

supervisedLearning = SupervisedLearning(DataInfo.firstTrainingStartTime, DataInfo.firstTrainingEndTime, DataInfo.secondTrainingStartTime, DataInfo.secondTrainingEndTime, DataInfo.firstTestingStartTime, DataInfo.firstTestingEndTime, DataInfo.secondTestingStartTime, DataInfo.secondTestingEndTime)
supervisedLearning.GenerateSVMModel()
supervisedLearning.Validate()
