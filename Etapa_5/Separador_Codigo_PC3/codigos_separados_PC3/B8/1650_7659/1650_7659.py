from numpy import *

cabelos = input("digite: ").upper().split(',')

soma = zeros(5, dtype=int)

for i in range(size(cabelos)):
	if cabelos[i] == 'P' :
		soma[0] = soma[0] + 1
	elif cabelos[i] == 'C':
		soma[1] = soma[1] + 1
	elif cabelos[i] == 'R':
		soma[2] = soma[2] + 1
	elif cabelos[i] == 'L':
		soma[3] = soma[3] + 1
	elif cabelos[i] == 'B':
		soma[4] = soma[4] + 1

print(max(soma))
print(soma)