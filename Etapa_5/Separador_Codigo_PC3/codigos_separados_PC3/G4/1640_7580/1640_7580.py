from numpy import *
x = array(eval(input(': ')))
c = 0
for i in range(size(x)):
	if x[i] % 2 != 0:
		c += 1
print(c)
v = zeros(c,dtype=int)
c = 0 
for i in range(size(x)):
	if x[i]%2 != 0:
		v[c] = i
		c += 1
print(v)