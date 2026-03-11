from numpy import*

string = input("digite:")
i = 0 

while i < size(string):
	if string[-1] == "n" or string[-1] == "N":
		print(string.upper())
	elif string[-1] != "n" or string[-1] !=  "N":
		print("nome invalido")
	i = i + 1