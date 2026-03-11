a = float(input("Consumo de energia: "))

b = (0.6*a)+5
c = (0.75*a) + 16
			 
if (a <= 150):
	print(round(b, 2))
else:
	print(round(c, 2))