peso = float(input("insira o peso do tripulante: "))

if peso > 3000 or peso < 4500:
	if peso >= 3000 and peso < 3400:
		total = peso * 0.8
		print(round(total, 1))
	elif peso >= 3400 and peso < 3900:
		total = peso * 1.3
		print(round(total, 1))
	elif peso >= 3900 and peso < 4100:
		total = peso * 2.1
		print(round(total, 1))
	else:
		total = peso * 3.0
		print(round(total, 1))