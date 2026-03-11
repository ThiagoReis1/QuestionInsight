from numpy import *

vet = input("digite a etiqueta").upper()
i = len(vet)
cont = 0
preco = 0
while(cont < i):
	if( vet[cont] == 'A' or vet[cont] == 'E' or vet[cont] == 'I' or vet[cont] == 'O' or vet[cont] == 'U'):
		preco = preco + 0.15
	else:
		preco = preco + 0.17
	cont = cont + 1
print(round(preco,2))