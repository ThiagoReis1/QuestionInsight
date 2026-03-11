from numpy import *
x = input("nome : ")

if x[-1] == "s" or x[-1] == "S":
	print(x.upper())
else:
	print("nome invalido")
