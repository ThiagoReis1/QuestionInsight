from numpy import*
nome = input("digite o nome: ")

if len (nome) >= 5 and (nome[4].lower() == 'c'):
	print(nome.upper())
else:
	print("nome invalido")