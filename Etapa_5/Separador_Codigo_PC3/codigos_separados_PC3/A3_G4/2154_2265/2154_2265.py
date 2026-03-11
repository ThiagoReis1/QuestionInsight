from numpy import *
from math import *
P = array(eval(input("P:")))
Q = array(eval(input("Q:")))
a = 0
d = 0
for x in range(size(P)):
	d = d + ((P[x] - Q[x]) ** 2)
	l = sqrt(d)
print(round(l,4))
sim = (1/(1 + l))
print(round(sim, 2))