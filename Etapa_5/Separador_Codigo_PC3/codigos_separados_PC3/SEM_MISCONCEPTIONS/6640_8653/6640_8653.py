# faça seu código aqui!
from numpy import *
string = input().upper()
i = 0
cont = 0
while i < len(string):
	if string[i] == "N":
		print(i)
		cont = cont + 1	
	i = i + 1
if cont == 0:
	print("nao achei")

	