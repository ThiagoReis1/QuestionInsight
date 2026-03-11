# faça seu código aqui!
from numpy import*

string = input("digite uma palavra: ").upper()

cont = 0
i = 0
	
tamanho = len(string)

while i < tamanho:
	if string[1] == "P":
		cont +=1
	i+=1
		print(cont)
	else:
		print("nao achei")