# faça seu código aqui!
from numpy import * 
palavra = input("digite aqui: ").upper()

i = 0 
d = 0 
while i < len(palavra): 
	if palavra[i] == "P":
		print(i)
	i+=1
if "P" not in palavra:
	print("nao achei")


