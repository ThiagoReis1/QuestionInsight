from math import*
consumo = float(input("Consumo de agua: "))

if consumo >= 0.0 and consumo <= 10.0:
	valor = consumo * 3.00 + 15.00
	print(round(valor, 2))
elif consumo >= 10.0 and consumo <= 15.0:
	valor = consumo * 3.50 + 20.00
	print(round(valor, 2))
elif consumo >= 15.00 and consumo <= 20.0:
	valor = consumo * 4.00 + 25.00
	print(round(valor, 2))
elif consumo >= 20.00:
	valor = consumo * 4.50 + 30.00
	print(round(valor, 2))