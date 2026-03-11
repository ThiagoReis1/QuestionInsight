C = float(input("Consumo de agua: "))
T = 30.00
if(C <=10):
	V = C*3.00+T
	print(round(V, 2))
else:
	V = C*3.50+30.00
	print(round(V, 2))