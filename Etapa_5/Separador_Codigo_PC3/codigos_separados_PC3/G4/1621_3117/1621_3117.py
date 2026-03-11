from numpy import *

nome = array(eval(input("nomes dos produtos: ")))
quant = array(eval(input("quantidade: ")))

c = 0
soma = 0

while c < size(nome):
	if nome[c].lower() == "arroz":
		soma = soma + (1.25 * quant[c])
	
	elif nome[c].lower() == "feijao":
		soma = soma + (2.60 * quant[c])
	
	elif nome[c].lower() == "bis":
		soma = soma + (1.80 * quant[c])
	
	elif nome[c].lower() == "miojo":
		soma = soma + (0.85 * quant[c])
	
	else:
		soma = soma + (3.20 * quant[c])
		
	c = c + 1
	
print(round(soma,2))