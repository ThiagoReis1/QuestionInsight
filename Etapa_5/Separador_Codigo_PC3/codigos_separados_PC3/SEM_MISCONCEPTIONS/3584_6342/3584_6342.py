from numpy import *
desc = array(eval(input('Digite a quantidade de compras')))
i = 0
compras = 1
while i <size(desc):
	if desc[i] > 200:
		
		compras = desc * 0.85
	elif desc[1] < 200:	
	i = i + 1

print(compras)