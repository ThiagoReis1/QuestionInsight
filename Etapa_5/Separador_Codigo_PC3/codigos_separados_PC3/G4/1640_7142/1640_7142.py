from numpy import *

v = array(eval(input()))

s = 0 
p = 0

for i in range(size(v)):
	if(v[i] % 2 != 0):
		s = s + 1
print(s)

x = zeros(s, dtype = int)

for j in range(size(v)):
	if(v[j] % 2 != 0):
		x[p] = j
		p = p + 1
print(x)