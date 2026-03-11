from numpy import *

carta = array(input("informe a sequencia de caracteres de cartas: "))
naipes = [0, 0, 0, 0]

for carta in carta:
	if carta == 'C':
		naipes[0] += 1
	elif carta == 'O':
		naipes[1] += 1
	elif carta == 'P':
		naipes[2] += 1
	elif carta == 'E':
		naipes[3] += 1
		
print(naipes)