quantidade = int(input('digite a quantidade: '))

if quantiade < 10:
	custo = 50 + 5.50
elif quantidade == 10:
	custo = 50 + 7.75
else:
	custo = 50 + 10
print('total=', round(custo, 2))
