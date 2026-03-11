from numpy import *
vet = array(eval(input("Digite o preco dos doces comprados:")))

cont = 0 
soma = 0

for i in range(size(vet)):
	if vet[i] > 20:
		soma = soma  + vet[i]
		cont = cont + 1

		
media = soma/cont
print(round(media,2))

