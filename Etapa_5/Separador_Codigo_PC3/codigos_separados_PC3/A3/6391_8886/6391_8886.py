from numpy import *
numero = array(eval(input(" ")))

vetor= zeros() 

for i in numero:
	if 0 <= numero <= 9:
		numero = numero * 3

	else:
		print(numero)