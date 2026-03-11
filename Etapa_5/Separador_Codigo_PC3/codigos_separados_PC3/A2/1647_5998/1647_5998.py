from numpy import *
v = array(eval(input()))

aprov = 0
reprov = 0
for i in range(0,size(v)):
	if v[i]<70:
		reprov = reprov + 1
	else:
		aprov = aprov + 1
print(aprov)

c = 0
z = zeros(aprov, dtype=int)
for i in range(0,size(v)):
	if v[i]>=70:
		z[c]=i
		c = c + 1
	else:
		c = c
print(z)