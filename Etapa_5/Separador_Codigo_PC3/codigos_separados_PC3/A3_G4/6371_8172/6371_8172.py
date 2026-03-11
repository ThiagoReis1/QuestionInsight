from numpy import *

v = array(eval(input()))

x = zeros(range(size(v)), dtype=int)

for i in range(size(v)):
	if v[i] == 0:
		v[i] = 9**2
	else:
		v[i] = (v[i] - 1)**2
print(v)
	