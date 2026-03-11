from numpy import *
u = array(eval(input()))
a = 0
c = 0
for i in range(size(u)):
	if u[i] > 180:
		a += 1
		c += u[i]
		m = c/a
if a == 0:
	m = 0.0
print(round(m, 2))