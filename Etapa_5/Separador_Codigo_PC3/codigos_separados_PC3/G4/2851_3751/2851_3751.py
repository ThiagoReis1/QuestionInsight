from numpy import *

vet = array(eval(input()))

soma = 0

for val in vet:
	soma += val
	if val == 99:
		soma -= val
		soma *= 2

print(soma)