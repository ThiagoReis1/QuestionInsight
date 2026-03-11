v = float(input("Digite o valor em metros cubicos: "))
cb = (3 * v) + 30
ca = (3.50 * v) + 30
if(v < 10):
	print(round(cb, 2))
else:
	print(round(ca, 2))
	