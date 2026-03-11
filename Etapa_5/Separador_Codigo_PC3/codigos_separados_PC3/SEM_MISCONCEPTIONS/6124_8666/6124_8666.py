peso = float(input("digite o peso em gramas: "))

if peso < 4100 and peso >= 3900:
	total = peso * 2.1
	print(round(total , 1))
elif peso < 3900 and peso >= 3400:
	total = peso * 1.3
	print(round(total , 1))
elif peso < 3400 and peso >= 3000:
	total = peso * 0.8
	print(round(total , 1))
else:
	total = peso * 3000
	print(round(total , 1))