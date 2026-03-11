v = float(input(''))

if v <= 10:
	valor = v * 3 + 15
	print(round(valor, 2))
	
elif v <= 15:
	valor = v * 3.5 + 20
	print(round(valor, 2))
	
elif v <= 20:
	valor = v * 4 + 25
	print(round(valor, 2))

elif v >= 20:
	valor = v * 4.5 + 30
	print(round(valor, 2))