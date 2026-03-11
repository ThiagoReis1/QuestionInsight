c = float(input("consumo de agua: "))

if (c < 10):
	t = c * 3.00 + 30.00
	print(round(t,2))
	
else:
	t2 = c * 3.50 + 30.00
	print(round(t2,2))