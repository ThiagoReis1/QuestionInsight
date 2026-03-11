from numpy import *

v = array(eval(input()))
v0 = zeros(size(v), dtype=int)

for i in range(size(v)):
	if v[i] != 0:
		v0[i] = (v[i] - 1) ** 2
	elif v[i] == 0:
		v0[i] = 9 ** 2
print(v0)