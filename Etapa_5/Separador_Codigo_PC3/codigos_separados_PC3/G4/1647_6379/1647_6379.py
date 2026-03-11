from numpy import *
x = array(eval(input()))
c = 0
for i in x:
	if i >= 70:
		c = c + 1
print(c)
z = zeros(c,dtype = int)
d = 0
for i in range(size(x)):
	if x[i] >= 70:
		z[d] = i
		d = d + 1
print(z)