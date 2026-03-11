from numpy import*
from math import*
P = array(eval(input()))
Q = array(eval(input()))
t = 0
for i in range(size(P)):
	t = t + (P[i] - Q[i])**2
print(round(sqrt(t),4))
