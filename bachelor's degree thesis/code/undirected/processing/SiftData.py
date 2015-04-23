#Author: Kai Huang
#Date: 2015.04.02

import sys
sys.path.append("../tools")
import StringProcessing
lines = open("../../../data/facebook-wosn-wall/sorted_out.facebook-wosn-wall", "r")
lines2004_2006 = open("../../../data/facebook-wosn-wall/edges2004_2006.facebook-wosn-wall", "w")
lines2007 = open("../../../data/facebook-wosn-wall/edges2007.facebook-wosn-wall", "w")
lines2004_2007 = open("../../../data/facebook-wosn-wall/edges2004_2007.facebook-wosn-wall", "w")
lines2008 = open("../../../data/facebook-wosn-wall/edges2008.facebook-wosn-wall", "w")
for line in lines:
	tokens = StringProcessing.SplitLine(line)
	if tokens[4] <= "2006":
		lines2004_2006.write(tokens[0] + ' ' + tokens[1] + '\n')
	if tokens[4] == "2007":
		lines2007.write(tokens[0] + ' ' + tokens[1] + '\n')
	if tokens[4] <= "2007":
		lines2004_2007.write(tokens[0] + ' ' + tokens[1] + '\n')		
	if tokens[4] == "2008":
		lines2008.write(tokens[0] + ' ' + tokens[1] + '\n')
lines2004_2006.close()
lines2007.close()
lines2004_2007.close()
lines2008.close()