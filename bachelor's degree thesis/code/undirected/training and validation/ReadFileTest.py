###change key from float to int###
# import pickle
# import copy

# rfile = open("./temp data/Vectors1970_1979/Vectors")
# test = pickle.load(rfile)
# newTestFile = open("./temp data/Vectors1970_1979/Vectors_tmp", 'w')

# for i in test.keys():
# 	for j in test[i].keys():
# 		for k in test[i][j].keys():
# 			temp = copy.copy(test[i][j][k])
# 			del test[i][j][k]
# 			test[i][j][int(k)] = temp
###change key from float to int###

# pickle.dump(test, newTestFile)

# from svmutil import *
# # Read data in LIBSVM format
# y, x = svm_read_problem('./heart_scale')
# m = svm_train(y[:200], x[:200], '-c 4')
# p_label, p_acc, p_val = svm_predict(y[200:], x[200:], m)


import pickle

rfile = open("./temp data/PartitionSets1970_1979")
test = pickle.load(rfile)
for i in test:
	print i
