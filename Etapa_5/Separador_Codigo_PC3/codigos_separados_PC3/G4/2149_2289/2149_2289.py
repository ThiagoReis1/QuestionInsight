from numpy import *
v1 = array(eval(input()))
v2 = array(eval(input()))

a = 0
k = zeros(size(v1), dtype = float)
for i in range(size(v1)):
	k[i] = v1[i] + v2[i]
	if k[i] >= 12:
		a = a + 1

print(k)
print(a)
