from numpy import *
c = array(eval(input()))
v = zeros(size(c), dtype=int)

for i in range(size(c)):
	if c[i] == 9:
		v[i] = 0
	else:
		v[i] = c[i] + 1
print(v)