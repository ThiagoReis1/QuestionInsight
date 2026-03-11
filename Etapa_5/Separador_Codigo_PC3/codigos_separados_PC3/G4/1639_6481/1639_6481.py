from numpy import *

v = array(eval(input()))
a = 0 

for i in range(size(v)):
	if(v[i] % 2 == 0):
		a = a + 1
		
x = zeros(a, dtype = int)
y = 0

for i in range(size(v)):
	if(v[i] % 2 == 0):
		x[y] = i
		y = y + 1

print(a)
print(x)
	