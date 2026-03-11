x = float(input("Digite um numero: "))

if (x <= 1):
	print(1)
	
elif (x > 1 and x <= 2):
	print(2)
	
elif (x > 2 and x <= 3):
	y = x ** 2
	print(round(y,2))
	
else:
	if (x > 3):
		y = x ** 3
		print(round(y,2))