from numpy import *
v = array(eval(input()))
c = 0
for i in range(0,size(v)):
	if (v[i]!=99):
		c = c + v[i]
	else:
		c = c * 2
print(c)