from numpy import *

v = array(eval(input()))

j = 0
for i in range(size(v)):
	if v[i] < 70:
		j += 1
print(j)

r = zeros(j, dtype=int)

c = 0
for i in range(size(v)):
	if v[i] < 70:
		r[c]= i
		c += 1
print(r)

