from numpy import *
n = int(input())
m = zeros((n,n),dtype=int)
for i in range(shape(m)[0]):
	for j in range(shape(m)[1]):
		if i == j:
			m[i,j] = 1
		elif i > j:
			m[i,j] = 0
		elif i < j:
			m[i,j] = 1
print(m)