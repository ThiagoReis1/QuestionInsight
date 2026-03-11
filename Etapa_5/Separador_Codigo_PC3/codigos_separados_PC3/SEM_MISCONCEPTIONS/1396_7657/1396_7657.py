valor = float(input("valor: "))
if valor <= 300:
	x = (10/100 * valor) + valor
	print(round(x, 2))
else:
	y = (6/100 * valor) + valor 
	print(round(y, 2))	