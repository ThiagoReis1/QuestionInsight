from math import*
consumo = float(input("consumo de energia: "))
menor = (consumo * 0.60) + 5
maior = (consumo * 0.75) + 16
if (consumo <= 150):
	print(round(menor, 2))
else:
	print(round(maior, 2))