# faça seu código aqui!
from numpy import*
string = input().upper()
i = 0
cont = 0
while i < len(string):
	if string[i] == "P":
		print(i)
	i += 1
	
if "P" not in string:
	print("nao achei")