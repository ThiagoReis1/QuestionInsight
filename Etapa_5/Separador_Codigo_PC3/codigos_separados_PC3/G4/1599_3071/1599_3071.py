from numpy import *
v = array(eval(input("digite: ")))
i = 0
c = 0 
while(i < size(v)):
	if (v[i] > 80):
		d = v[i] * 15 / 100
		c = c - d 
	c = c + v[i]
	i = i + 1
print(round(c, 2))