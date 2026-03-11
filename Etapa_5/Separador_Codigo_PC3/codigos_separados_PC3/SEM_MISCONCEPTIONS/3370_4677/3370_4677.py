unidade = input('unidade de medida: ')
valor = float(input('valor medida'))
if(unidade == 'C'):
   conv = 0.393701 * valor
else:
	conv = valor / 0.393701
print(round( conv, 2))

