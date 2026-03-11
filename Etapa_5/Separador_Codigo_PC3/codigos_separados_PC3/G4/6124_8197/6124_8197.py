peso = float(input("Peso do tripulante: "))

if (peso >= 3000 and peso < 3400):
	print(peso * 0.8)
elif (peso >= 3400 and peso < 3900):
	print(peso * 1.3)
elif (peso >= 3900 and peso < 4100):
	print(peso * 2.1)
else:
	print(peso * 3)