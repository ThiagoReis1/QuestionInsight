from numpy import*

string = input("insira o nome: ").upper()

if string[-1] == "S":
	print(string.upper())
else:
	print("nome invalido")