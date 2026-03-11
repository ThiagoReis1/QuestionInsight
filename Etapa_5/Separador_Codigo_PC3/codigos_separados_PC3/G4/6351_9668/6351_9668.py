from numpy import *

nome = input("nome: ").upper()

if nome[-1] == "S":
	print(nome)
	
else:
	print("nome invalido")