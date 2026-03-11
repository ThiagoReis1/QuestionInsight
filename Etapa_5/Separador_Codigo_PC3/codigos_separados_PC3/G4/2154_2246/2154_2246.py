from numpy import*
from math import*
p= array(eval(input(":")))
q= array(eval(input(":")))
d= 0
for i in range(size(p)):
	 d = d + ((p[i]-q[i])**2)

l = sqrt(d)
print(round(l,4))
sim = (1/(1+l))
print(round(sim,2))
	