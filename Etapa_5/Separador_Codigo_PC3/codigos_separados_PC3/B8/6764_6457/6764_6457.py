peso = float(input("Digite o numero: "))

if peso < 5:
	custo = 10.0 + 3.75
	print(round(custo, 2))
elif peso == 5:
	custo = 10.0 + 4.75
	print(round(custo, 2))
elif peso > 5:
	custo = 10.0 + 5.75
	print(round(custo, 2))