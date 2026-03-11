# faça seu código aqui!
from numpy import*

vet = input("palavra: ").upper()

i = 0
cont = 0

if i < len(vet):
	if vet[i] != 'D':
		cont = cont + 1
	i = i + 1
print(cont)