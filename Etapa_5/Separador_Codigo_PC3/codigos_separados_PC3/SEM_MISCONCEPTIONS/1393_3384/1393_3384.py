peso = float(input("peso em gramas: "))

if (peso < 5000):
	valor1 = peso * 0.05
	print(round(valor1, 2))
else:
	valor2 = peso * 0.04 + 60
	print(round(valor2, 2))