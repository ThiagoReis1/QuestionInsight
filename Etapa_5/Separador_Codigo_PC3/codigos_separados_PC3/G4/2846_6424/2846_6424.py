from numpy import *
v = array(eval(input()))
z = zeros(size(v),dtype=int)
for c in range(size(v)):
	z[c] = 2 * v[c]
print(z)