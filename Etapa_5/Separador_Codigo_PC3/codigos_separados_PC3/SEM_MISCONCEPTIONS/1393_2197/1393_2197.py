p = float(input("Digite valor de p: "))

if p < 5000:
	frete = (5000*0.05)
	print(round(frete, 2))
if p >= 5000:
	frete = (5000*0.04)+60.00
	print(round(frete, 2))