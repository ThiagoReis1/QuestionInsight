from numpy import *

vet = input("escreva ").upper().split(',')
vet1 = input("palavra").upper()

vet1 =  vet1.replace("R", "L")

resposta = 500
for x in range(size(vet)):
	if(vet1== vet[x]):
		resposta = x

if resposta == 500:
	print("NAO ENCONTRADA")
else:
	print(resposta)

