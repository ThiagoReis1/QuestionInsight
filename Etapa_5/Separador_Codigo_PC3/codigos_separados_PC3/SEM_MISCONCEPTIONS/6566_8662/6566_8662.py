quantidade = int(input('Digite a quantidade: '))

if quantidade < 10:
	custo = 30 + 3.25
elif quantidade == 10:
	custo = 30 + 4.50
else:
	custo = 30 + 6.00
	
print('total=', round(custo, 2))