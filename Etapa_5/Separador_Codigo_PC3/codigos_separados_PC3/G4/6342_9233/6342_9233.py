from numpy import*
nome = input(" ")

if len (nome) >= 1 and (nome[0].lower() == "m"):
	print(nome.upper())

else:
	print("nome invalido")