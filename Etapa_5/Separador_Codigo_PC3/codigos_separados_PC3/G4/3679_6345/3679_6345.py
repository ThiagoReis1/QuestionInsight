from numpy import *

dp = 0
vet = int(input("n: "))

mat0 = zeros([vet,vet], dtype=int)

for i in range(shape(mat0)[0]):
	for j in range(shape(mat0)[1]):
		if i == j:
			dp = dp + mat0[i,j]
			mat0[i,j] = dp + 1
			
		if i < j:
			mat0[i,j] = dp + 1
		

print(mat0)