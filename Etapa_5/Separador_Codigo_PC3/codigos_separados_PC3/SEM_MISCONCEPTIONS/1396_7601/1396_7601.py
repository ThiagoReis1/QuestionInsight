valor_c = float(input("Insira o valor consumido no restaurante: "))

if valor_c <= 300:
	x = (valor_c * 0.1) + valor_c
	print(round(x, 2))
else:
	x = (valor_c * 0.06) + valor_c
	print(round(x,2))