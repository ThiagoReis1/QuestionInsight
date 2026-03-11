from numpy import*
nome = input("Digite um nome: ")

if nome[-1].lower() == 's':
	print(nome.upper())	
else:
	print("nome invalido")