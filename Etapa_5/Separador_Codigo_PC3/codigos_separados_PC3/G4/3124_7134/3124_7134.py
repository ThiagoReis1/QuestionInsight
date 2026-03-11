from numpy import *
v = array(eval(input("numero:")))
m = 1

for i in range(size(v)):
	m = m * v[i]
	
m = m**(1/size(v))
print(round(m, 2))