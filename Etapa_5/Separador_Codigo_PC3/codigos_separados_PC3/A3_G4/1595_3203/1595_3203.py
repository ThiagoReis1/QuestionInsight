from numpy import *

v = array(eval(input()))

x=0
m=0

while (x<size(v)) :
	if v[x]>0:
		m = (v[0]+v[1]+v[2])/3 - min(v[1])
		x = x+1
print(round(m,2))