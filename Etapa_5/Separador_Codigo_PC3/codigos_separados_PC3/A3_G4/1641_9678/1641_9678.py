from numpy import *

x = array(eval(input(":")))
y = zeros(x, dtype = int)
z = 0
for i in (x):
	if i % 3 == 0:
		z += 1
print(z)
y = zeros(z, dtype = int)
z = 0
for i in range(size(x)):
	if x[i] % 3 == 0:
		y[z] = i
		z += 1
print(y)
