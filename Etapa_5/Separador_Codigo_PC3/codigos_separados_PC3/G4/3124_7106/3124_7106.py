from numpy import *

v = array(eval(input()))
m = 1
for i in range(size(v)):
	m = m * v[i]

print(round(m**(1/size(v)), 2))