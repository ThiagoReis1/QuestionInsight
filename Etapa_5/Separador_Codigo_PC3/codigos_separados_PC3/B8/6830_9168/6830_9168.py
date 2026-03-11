from numpy import *

produto = input()
valor = 0
i = 0

while i < len(produto):
	if produto[i].upper() == "H":
		valor = valor + 3.85
		i +=1
	elif produto[i].upper() == "L":
		valor = valor + 2.95
		i += 1
	elif produto[i].upper() == "E":
		valor = valor + 7.90
		i+= 1
print(round(valor, 2))
		
	
	
		
