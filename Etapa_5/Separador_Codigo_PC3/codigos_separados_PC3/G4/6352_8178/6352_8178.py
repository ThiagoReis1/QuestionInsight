from numpy import*

nome = input("digite um nome: ")
if nome[-1].lower() == "n":
	print(nome.upper())
else:
	print("nome invalido")