a = input("unidade da medida: (K/L) ")
b = float(input("valor da medida: "))

if (a.upper() == "K"): 
	x = b * 2.35215 
	print(round(x, 2))
else:
	d = b / 2.35215
	print(round(d, 2))