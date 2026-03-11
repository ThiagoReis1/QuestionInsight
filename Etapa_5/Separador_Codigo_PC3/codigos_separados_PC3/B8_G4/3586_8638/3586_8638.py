from numpy import *

vet = array(eval(input(":")))
i = 0
cont = 0

while i < size(vet):
	if vet[i] == 1:
		cont = cont + 100
	elif vet[i] == 2:
		cont = cont + 60
	elif vet[i] == 3:
		cont = cont + 20
	elif vet[i] == 2:
		cont = cont + 0
	i = i + 1
print(cont)