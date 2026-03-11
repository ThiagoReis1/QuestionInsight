peso = int(input("digite o valor: "))


if peso <= 5000 and peso >= 0:
	valor = peso * 0.03 + 20
	print(round(valor, 2))
elif peso <= 5001 and peso <= 6000:
	valor = peso * 0.04 + 25
	print(round(valor, 2))
elif peso >= 6001 and peso <= 7000:
	valor = peso * 0.05 + 30
	print(round(valor, 2))
else:
	valor = peso * 0.06 + 35
	print(round(valor, 2))