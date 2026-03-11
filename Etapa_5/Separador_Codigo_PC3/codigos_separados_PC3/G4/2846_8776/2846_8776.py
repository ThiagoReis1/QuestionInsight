from numpy import *
n = array(eval(input()))
v = zeros(size(n), dtype=int)
for i in range(size(n)):
	v[i] = n[i]*2
print(v)