a=float(input("consumo: "))
if(a<10):
	b = 30+(a*3.00)
	print(round(b,2))
else:
	b = 30+(a*3.50)
	print(round(b,2))