from numpy import *

k = array(eval(input()))
k1 = zeros(size(k), dtype=int)			 

for x in range(size(k)):
	if k[x] == 9:
		k1[x] = 0
	else:
		k1[x] - 1 = k[x] + 1 **3
print(k1)
	
	