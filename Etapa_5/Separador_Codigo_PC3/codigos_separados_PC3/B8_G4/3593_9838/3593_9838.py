from numpy import *

f = array(eval(input("vetor: ")))
p = array([0.5,3])

i=0
c=200

while i < size(f):
	if f[i] == 1 or f[i] == 3 or f[i] == 5:
		c = c*p[0]
	elif f[i] == 2 or f[i] == 4 or f[i] == 6:
		c = c*p[1]
	i=i+1
	
print(c)