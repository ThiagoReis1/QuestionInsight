# faça seu código aqui!
from numpy import*
string = input("palavra: ").upper()
i = 0
ls = 0
while i < len(string):
	if string[i] == "L":
		print(i)
	i = i +1
if "L" not in string:		
	print("nao achei")
	
	
