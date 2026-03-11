import numpy as np

valor = input()

contador_b = 0
contador_c = 0
contador_e = 0
valor_pagar = 0

i = 0
while i < len(valor):
	if valor[i].upper() == 'B':
		contador_b += 1
		
		valor_pagar = valor_pagar + 3.75
	
	elif valor[i].upper() == 'C':
		contador_c += 1
		
		valor_pagar = valor_pagar + 7.90
		
	else:
		contador_e += 1
		valor_pagar = valor_pagar + 9.85
	
	i+= 1
	
print('{} {} {} {}'. format(round(valor_pagar, 2), contador_b, contador_c, contador_e))