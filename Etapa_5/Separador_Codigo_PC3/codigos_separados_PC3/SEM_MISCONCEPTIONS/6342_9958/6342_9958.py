from numpy import *

nome = input("nome")
letra = nome[0].lower()
if letra == "m":
	print (nome.upper())
else:
	print("nome invalido")