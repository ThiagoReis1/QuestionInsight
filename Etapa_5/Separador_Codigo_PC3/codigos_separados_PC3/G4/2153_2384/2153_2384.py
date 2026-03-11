from numpy import*
from math import*

p = array(eval(input("v1: ")))
q = array(eval(input("v2: ")))
i = 0
d = 0

while(size(p)>i):
	d = (p[i]-q[i])**2 + d
	i = i + 1
print(round(sqrt(d),4))

