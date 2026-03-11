from numpy import *

itens = array(eval(input("insira os itens comprados: ")),dtype=float)
total = 0

for g in range(size(itens)):
	if(itens[g] > 40):
		itens[g] = itens[g] - 2.50
	total = total + itens[g]
	
print(round(total,2))