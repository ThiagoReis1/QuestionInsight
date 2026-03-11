r =  217
from numpy import*
v = array(eval(input("levantamentos: ")))
s = size(v)
x = 0
n = 0
while (s > 0):
	if (v[0 + x] > 217):
		n = n + 1
	x = x + 1
	s = s - 1
print (r)
print (n)