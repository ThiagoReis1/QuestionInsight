from numpy import *
nome = input("digite um nome: ").upper()
i = 0
valor = 0

while(i < len(nome)):
	if(nome[i] == "A"):
		valor = 45.12 + valor
	elif(nome[i] == "E"):
		valor = 45.12 + valor
	elif(nome[i] == "I"):
		valor = 45.12 + valor
	elif(nome[i] == "O"):
		valor = 45.12 + valor
	elif(nome[i] == "U"):
		valor = 45.12 + valor
	else:
		valor = 50.18 + valor
	i= i+1

print(valor)