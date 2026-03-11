from numpy import *

etnia = array(eval(input("Digite a etnia: "))).upper().split(',')

cont = 0
soma = 0
for x in etnia:
	if(etnia == 'B'):
		cont = cont + 1
	elif(etnia == 'PA'):
		cont = cont + 1
	elif(etnia == 'PR'):
		cont = cont + 1
	elif(etnia == 'A'):
		cont = cont + 1
	elif(etnia == 'I'):
		cont = cont + 1
print(max(cont))
print(cont(0,6))
	
