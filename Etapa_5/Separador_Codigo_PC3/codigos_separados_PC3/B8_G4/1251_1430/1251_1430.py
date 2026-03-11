from numpy import *
v = array(eval(input()))
x = zeros(2,dtype=int)
a = min(v)
b = max(v)
c = 0.7 * a + 0.3 * b
d = 0.4 * a + 0.6 * b
for i in range(size(v)):
	if (v[i] >= c) and (v[i] < d):
		x[0] += 1
	elif (v[i] >= d) and (v[i] < b):
		x[1] += 1
print(x)		