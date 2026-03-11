from numpy import *
v =  array(eval(input("")))

c = 0


for i in range(size(v)):
	if (v[i] % 5 == 0):
		c = c + 1
print(c)
c2 = 0
v2 = zeros(c, dtype=int)
for j in range(size(v)):
	if (v[j] % 5 == 0):
		v2[c2] = j
		c2 = c2 + 1
print(v2)
