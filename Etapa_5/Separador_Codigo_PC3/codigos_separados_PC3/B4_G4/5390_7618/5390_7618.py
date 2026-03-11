from numpy import *

nome=input("apenas letras: ").upper()

i = 0
soma = 0
while i < len(nome):
	if nome[i] == "A":
		soma = soma + 0.19
	elif nome[i] == "E":
	 	soma = soma + 0.19
	elif nome[i]=="I":
		soma= soma + 0.19
	elif nome[i] == "O":
		soma = soma +0.19
	elif nome[i] == "U":
		soma = soma + 0.19
	else:
		soma = soma + 0.23
	i = i + 1
print(round(soma,2))
		
