from numpy import *
lista = input()

resultado = zeros(4, dtype = int)

for i in lista:
	if i == 'A':
		resultado[0] +=1
	elif i == 'B':
		resultado[1] +=1
	elif i == 'L':
		resultado[2] +=1
	elif i == 'H':
		resultado[3] +=1
		
		
print(resultado)