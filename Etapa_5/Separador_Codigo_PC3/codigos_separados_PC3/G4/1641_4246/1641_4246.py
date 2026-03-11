from numpy import *

vet = array(eval(input()))

n = j = 0

for i in range(size(vet)):
	if(vet[i] % 3 == 0):
		n = n + 1
print(n)

res = zeros(n, dtype=int)

for i in range(size(vet)):
	if(vet[i] % 3 == 0):
		res[j] = i
		j = j + 1
print(res)