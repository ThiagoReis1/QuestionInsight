from numpy import *

a = array(eval(input()))
cont = 0

for i in range(len(a)):
	if a[i] >= 2000:
		cont += 1

c = zeros(cont, dtype = int)
k = 0

for j in range(len(a)):
	if (a[j] >= 2000):
		c[k] = j
		k += 1
		
print(cont)
print(c)
	

