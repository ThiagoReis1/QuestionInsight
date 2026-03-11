from numpy import*
from math import*
v1 = array(eval(input()))
v2 = array(eval(input()))
s = 0

for i in range(size(v1)):
	s = s + ((v1[i]-v2[i])**2)
d = sqrt(s)
sim = 1 / (1 + d)
print(round(d,4))
print(round(sim,2))
		

