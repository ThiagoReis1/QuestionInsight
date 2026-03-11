valor_consumido = float(input("qual o valor consumido:"))




if (valor_consumido <= 300):
	print (round(valor_consumido + valor_consumido * 0.10, 2))
else:
	print (round(valor_consumido + valor_consumido * 0.06, 2))