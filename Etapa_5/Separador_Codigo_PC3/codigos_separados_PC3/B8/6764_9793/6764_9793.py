peso = float(input('Peso: '))

if peso < 5:
	valor = 10 + 3.75
elif peso == 5:
	valor = 10 + 4.75
elif peso > 5:
	valor = 10 + 5.75
print(round(valor, 2))