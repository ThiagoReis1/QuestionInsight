consumo = float(input("Digite o consumo de minutos do cliente: "))
if consumo <= 100:
	valor = 1.20 * consumo
else:
	valor = 25 + (1.40 * consumo)
print(round(valor,2))