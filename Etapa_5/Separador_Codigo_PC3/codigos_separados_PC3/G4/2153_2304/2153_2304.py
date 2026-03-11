from numpy import*
from math import*
p = array(eval(input()))
q = array(eval(input()))
s = 0
for i in range(size(p)):
	s = s + (p[i] - q[i])**2
print(round(sqrt(s), 4))	