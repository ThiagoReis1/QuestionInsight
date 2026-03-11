a = int(input('codigo do cargo: '))
b = float(input("salario: "))


if a == 101:
	c = (10/100 * b) + b
	print(round(c, 2), "Aumento de 10 por cento")
else:
	d = (30/100 * b) + b
	print(round(d, 2), "Amento de 30 por cento")
	
	
