from numpy import*
from math import*
vetP = array(eval(input()))
vetQ = array(eval(input()))
t = 0 
for x in range(size(vetP)):
	t= t + (vetP[x] - vetQ[x] )**2
print(round(sqrt(t),4))