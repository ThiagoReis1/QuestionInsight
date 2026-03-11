from numpy import *

etiqueta = (input("Qual a etiqueta?: ")).upper()


soma = 0

for i in etiqueta:
	if i == "A":
		soma = soma + 0.25
		
	elif i == "E":
		soma = soma + 0.25
	
	elif i == "I":
		soma = soma + 0.25
	
	elif i == "O":
		soma = soma + 0.25
	
	elif i == "U":
		soma = soma + 0.25
		
	else:
		soma = soma + 0.27
 	
	
print(round(soma, 2))

