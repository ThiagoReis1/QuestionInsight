from numpy import * 
string = input("Digite um nome: ")

if string[2] == "r" or string[2] == "R":
	print(string.upper())
elif string[2] != "r" or string[2] == "R":
	print("nome invalido")
