c = float(input("Valor em metros cubicos: "))
cb = (3 * c) + 30
ca = (3.50 * c) + 30
if(c < 10):
	print(round(cb, 2))
else:
	print(round(ca, 2))