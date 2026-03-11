from numpy import *
freq = array(eval(input("")))
a = 0

for i in range(size(freq)):
	if freq[i] >= 70:
		a = a + 1
x = zeros(a , dtype = int)
p = 0
for i in range(size(freq)):
	if freq[i] >= 70:
		x[p] = i
		p = p +1
print(a)
print(x)



from math import*
from m
	
	