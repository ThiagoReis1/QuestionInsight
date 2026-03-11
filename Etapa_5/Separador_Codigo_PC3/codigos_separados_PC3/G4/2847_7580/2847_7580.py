from numpy import *
x = array(eval(input(': ')))
v = zeros(size(x),dtype=int)
for i in range(size(x)):
	v[i] = (x[i])**2
print(v)