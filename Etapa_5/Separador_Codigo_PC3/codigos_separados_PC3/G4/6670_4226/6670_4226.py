from numpy import *
v = array(eval(input("> ")))
m20 = 0
L = len(v)

c = 0

for i in range(L):
	if v[i] >= 20:
		c += +1
		m20 += +v[i]
if c == 0:
	res = 0
else:
	res = m20/c
	res = round(res,2)
print(res)
