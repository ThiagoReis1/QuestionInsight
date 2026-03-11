from numpy import *

itens = array(eval(input(": ")))
soma = 0

for item in itens:
	if item > 80.00:
		soma += (item - (item * 0.15))
	else:
		soma += item
			
print(round(soma, 2))