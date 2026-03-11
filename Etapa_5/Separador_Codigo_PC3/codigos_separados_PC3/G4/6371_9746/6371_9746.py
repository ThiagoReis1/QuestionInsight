from numpy import *

v = array(eval(input()))

for i in range(0, len(v)):
	if v[i] == 0:
		v[i] = 81
	else:	
		v[i] = (v[i] - 1)**2
	
print(v)
	
		
	