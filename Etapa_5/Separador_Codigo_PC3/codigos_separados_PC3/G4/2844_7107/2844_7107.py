from numpy import *

ve = array(eval(input()))
vv = []

for i in range(size(ve)):
	if(ve[i] == 0):
		ve[i] = 10
	
	vv.append(ve[i] - 1)
	
vv = array(vv)
print(vv)