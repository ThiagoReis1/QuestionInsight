from numpy import *
v = array(eval(input()))
cont = 0
for c in range(0, size(v)):
	if v[c] <= 50:
		cont += 1
z = zeros(cont,dtype=int)
y = 0
for c in range(0,size(v)):
	if v[c] <= 50:
		z[y] += c
		y += 1
	c += 1
print(cont)
print(z)
