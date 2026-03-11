from numpy import *

v = array(eval(input("")))

for i in range(size(v)):
	if(v[i] > 180):
		v[i] = v[i] + 1
		m = sum(v[i])/size(v[i])
print(round(m, 2))