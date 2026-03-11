from numpy import *
from math import *
p = array(eval(input("p: ")))
q = array(eval(input("q: ")))

d = 0
for i in range(0, size(p)):
	d = d + (p[i] - q[i])**2

print(round(sqrt(d), 4))