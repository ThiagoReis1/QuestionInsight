from numpy import*

x = (input("digite o nome: "))
if x[1].lower() == "u":
	print(x.upper())
elif x[1] != "u":
	print("nome invalido")