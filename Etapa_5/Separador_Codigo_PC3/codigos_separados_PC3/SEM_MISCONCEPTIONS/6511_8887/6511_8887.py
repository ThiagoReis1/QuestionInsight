entrada = input('Digite o tipo de entrada: *').upper()
quantidade = float(input('Quantidade desejada *'))

valor = quantidade * 25.90

if entrada.upper() == 'B':
	total = valor - valor * 0.10
else:
	total = valor
	
print(round(total, 2))