from numpy import *

v = array(eval(input()))
k = 0
j = 0
for i in range(size(v)):
	if v[i] > 20.0:
		k += 1
		j = v[i] + j
		
if k > 0:
	print(round(j / k, 2))
elif k == 0:
	print(0.0)