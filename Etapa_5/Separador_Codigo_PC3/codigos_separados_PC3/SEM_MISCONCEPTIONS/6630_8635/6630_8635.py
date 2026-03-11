# faça seu código aqui!
from numpy import*
 
letra = input("").upper()
i = 0
cont = 0
while i < len(letra):
	if letra[i] == "L":
		cont = cont + 1
		i = i + 1
print("achei um L na posicao")
	elif cont == 0:
		
		i = i + 1
print("nao achei")
	

