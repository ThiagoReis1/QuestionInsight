from numpy import *

string = input("Digite o codigo criado: ")

i = 0
#compr. da string
v = len(string)
total = 0

while(i < v):
	if((string[i] == "A") or (string[i] == "E") or (string[i] == "I") or (string[i] == "O") or (string[i] == "U")):
		total = total + 25.12
	else:
		total = total + 40.18
	i = i + 1
print(round(total,2))
	

