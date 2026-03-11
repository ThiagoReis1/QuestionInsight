valor_consumido = float(input("valor consumido: "))
if (valor_consumido <= 300):
	valor_total = valor_consumido + (10/100 * valor_consumido)
else:
	valor_total = valor_consumido + (6/100 * valor_consumido)
print (float(round(valor_total, 2)))