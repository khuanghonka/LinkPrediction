# import pickle

# rfile = open("./temp data/PathsDict1970_1979.txt")
# test = pickle.load(rfile)
# for i in test:
# 	for j in test[i]:
# 		for path in test[i][j]:
# 			print path[0], path[-1]
# 			break
timeSpan = "1970_1979"
number = 1
s = "./temp data/Vectors" + timeSpan + "/"+ str(number)
print s