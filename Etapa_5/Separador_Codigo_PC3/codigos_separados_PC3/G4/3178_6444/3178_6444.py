from numpy import *
v = array(eval(input()))

a = zeros(size(v),dtype=int)
x = 0
y = 1
for i in range(size(v)):
	if v[i] != a[i]:
		a[x] = v[i]
		x = x + 1
	else:
		a[-1 * y] = v[i]
		y = y + 1
print(a)