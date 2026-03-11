from numpy import *

v = array(eval(input()))
z = zeros(len(c), dtype = int)
c = 0
for i in range(0, len(v)):
	if v[i] % 5 == 0:
		c += 1
		x[i] = i
print(c)
print(x)
	
	