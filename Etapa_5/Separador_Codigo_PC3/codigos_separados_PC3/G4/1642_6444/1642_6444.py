from numpy import *
v = array(eval(input()))

cont = 0
for i in range(size(v)):
	if v[i] % 5 == 0:
		cont = cont + 1
print(cont)
a = zeros(cont,dtype=int)
b = 0
for i in range(size(v)):
	if v[i] % 5 == 0:
		a[b] = i
		b = b + 1
print(a)