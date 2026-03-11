from numpy import *
string = input("Digite um nome: ")
i = 0

while i < size(string):
	if string[4] == "c" or string[4] == "C":
		print(string.upper())
	elif string[4] != "c"or string[4] == "C":
		print("nome invalido")
	i = i + 1
	
	