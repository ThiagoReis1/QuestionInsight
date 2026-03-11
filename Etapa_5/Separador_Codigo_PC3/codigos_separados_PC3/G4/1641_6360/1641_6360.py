from numpy import *
v = array(eval(input()))

e = 0
for i in range(size(v)):
	if v[i] % 3 == 0:
		e = e + 1

b = zeros(e, dtype = int)
o = 0
for i in range(size(v)):
	if v[i] % 3 == 0:
		b[o] = i
		o = o + 1
print(e)
print(b)