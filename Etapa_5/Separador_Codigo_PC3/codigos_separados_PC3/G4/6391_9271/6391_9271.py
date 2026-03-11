from numpy import *

v = array(eval(input("v: ")))

for i in range(size(v)):
	if v[i] == 0:
		v[i] = (v[i] + 9) ** 3
	else:
		v[i] = (v[i] - 1) ** 3
		
print(v)