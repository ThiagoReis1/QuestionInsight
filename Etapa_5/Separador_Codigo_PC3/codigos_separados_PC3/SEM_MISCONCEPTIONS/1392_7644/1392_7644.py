ca = float(input("Consumo de Agua: "))
if (ca < 10):
	mensagem = (3.00 * ca) + 30
else:
	mensagem = (ca * 3.50) + 30
print(round(mensagem, 2))