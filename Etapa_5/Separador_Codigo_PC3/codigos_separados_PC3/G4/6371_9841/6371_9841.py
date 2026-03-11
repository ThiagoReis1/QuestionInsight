from numpy import *
v = array(eval(input()))
for c in range(0, size(v)):
	if v[c] - 1 < 0:
		v[c] = 9**2
	else:
		v[c] = (v[c] - 1)**2
print(v)