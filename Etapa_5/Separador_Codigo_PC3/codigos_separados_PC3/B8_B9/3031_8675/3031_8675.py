x = float(input("insira o valor de x: "))

if x <= 1:
	print(1)
elif x > 1 and x <= 2:
	print(2)
elif x > 2 and x <= 3:
	total = x ** 2
	print(round(total, 2))
elif x > 3:
	total = x ** 3 
	print(round(total, 2))