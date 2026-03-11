from numpy import *	
from math import *
i = 0
p = array(eval(input()))
q = array(eval(input()))
t = 0

for i in range(size(p)):
	t = t + (p[i]- q[i])**2

print(round(sqrt(t),4))
