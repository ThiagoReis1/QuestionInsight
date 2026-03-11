from numpy import *
e = array(eval(input()))
c = 0
for i in range(0, size(e)):
	if e[i] % 5 == 0:
		c += 1
	i += 1
print(c)
a = zeros(c, dtype=int)
x = 0 
for i in range(0, size(e)):
	if e[i] % 5 == 0:
		a[x] += i
		x += 1
	i += 1
print(a)


	
	
		