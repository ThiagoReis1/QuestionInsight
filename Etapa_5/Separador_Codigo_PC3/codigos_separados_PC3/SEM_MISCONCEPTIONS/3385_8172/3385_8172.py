unidade = input().upper()
valor = float(input())

if unidade == 'H':
	acre = 2.47105 * valor
	print(round(acre, 2))
	
else:
	hectar = valor/2.47105
	print(round(hectar, 2))