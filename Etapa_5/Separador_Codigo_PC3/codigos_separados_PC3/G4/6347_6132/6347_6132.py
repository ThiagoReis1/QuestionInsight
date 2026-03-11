from numpy import *
nome = input("insira um nome: ")

for i in range(size(nome)):
	if nome[3] == "i" or nome[3] == "I":
		print(nome.upper())
	else:
		print("nome invalido")