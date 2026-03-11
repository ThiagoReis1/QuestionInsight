from numpy import *

a = array(eval(input()))
cont = 0

for i in range(size(a)):
	if a[i] >= 2000:
		cont += 1
print(cont)

ind = zeros(cont, dtype="int")
j = 0
for i in range(size(a)):
	if a[i] >= 2000:
		ind[j] = i
		j += 1
print(ind)