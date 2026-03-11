from numpy import *
from math import *
p = array(eval(input("p: ")))
q = array(eval(input("q: ")))
d = 0
for x in range(size(p)):
	d = d + ((p[x]-q[x])**2)
	l = sqrt(d)
print(round(l, 4))
sim = (1/(1+l))
print(round(sim, 2))