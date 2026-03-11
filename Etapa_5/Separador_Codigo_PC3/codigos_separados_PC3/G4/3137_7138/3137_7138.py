from numpy import*
from math import*

n = array(eval(input()))
i = 0 
g = 0
c = size(n)

while(i < size(n)):
	g = g + exp(n[i])
	i = i + 1
h = log(g/exp(c))

print(round(h,2))