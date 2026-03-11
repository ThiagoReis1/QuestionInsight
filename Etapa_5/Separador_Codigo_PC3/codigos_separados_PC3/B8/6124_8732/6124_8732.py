peso = float(input("Peso: "))

if (peso >= 3000) and (peso < 3400):
	valor = peso * 0.8
	print(round(valor, 1))
elif (peso >= 3400) and (peso < 3900):
	valor = peso * 1.3
	print(round(valor, 1))
elif (peso >= 3900) and (peso < 4100):
	valor = peso * 2.1
	print(round(valor, 1))
elif (peso >= 4100):
	valor = peso * 3
	print(round(valor, 1))