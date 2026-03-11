valor_consumido = float(input("Digite o valor consumido: "))

if(valor_consumido > 300):
	valor_gorjeta = valor_consumido * (6/100)
	valor_total = valor_consumido + valor_gorjeta
	print(round(valor_total,2))
else:
	valor_gorjeta = valor_consumido * (10/100)
	valor_total = valor_consumido + valor_gorjeta
	print(round(valor_total,2))