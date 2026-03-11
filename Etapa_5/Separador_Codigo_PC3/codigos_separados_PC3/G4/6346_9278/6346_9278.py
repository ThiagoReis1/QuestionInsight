from numpy import*

nome = input("digite o nome: ")

if len(nome)>= 5 and (nome[0]== "W"):
	print(nome.upper())
	
else:
	print("nome invalido")