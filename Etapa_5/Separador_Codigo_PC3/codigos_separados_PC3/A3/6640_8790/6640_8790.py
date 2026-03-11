# faça seu código aqui!
from numpy import*

string = input().upper()
i = 0
cont = 0
while i<len(string):
	if string[i]=="N":
		cont+=1
		print(i)
	i = i+1
if "N" not in string:
	print("nao achei")