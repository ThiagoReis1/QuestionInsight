from numpy import *

vet = array(eval(input('valor do produto: ')))

i = 0
j = 0

while i < size(vet):
	if vet[i] > 90.0:
		j = j + vet[i] - 6.50
	else:
		j = j + vet[i]
	
	i = i + 1

print(j)