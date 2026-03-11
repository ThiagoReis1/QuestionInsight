from numpy import *

entrada = array(eval(input()))

cont = 0
for elem in entrada:
	if(elem >= 2000):
		cont += 1
		
vet = zeros(cont, dtype=int)
j = 0
for i in range(len(entrada)):
	if(entrada[i] >= 2000):
		vet[j] = i
		j += 1
		
print(cont)
print(vet)