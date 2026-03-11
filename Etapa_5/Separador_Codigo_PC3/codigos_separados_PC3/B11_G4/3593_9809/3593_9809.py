from numpy import *
p = 200
n = array(eval(input()))
c = 0 
m = size(n)
while(c!=m):
	if (n[c]==1):
		p /=2
	if (n[c]==2):
		p *= 3
	if (n[c]==3):
		p /=2
	if (n[c]==4):
		p *= 3
	if (n[c]==5):
		p /= 2
	if (n[c]==6):
		p *= 3
	c += 1
print(round(p,2))