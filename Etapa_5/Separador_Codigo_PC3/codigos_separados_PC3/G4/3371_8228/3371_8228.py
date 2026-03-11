u = str(input("unidade (K/M): "))
v = float(input("valor da medida: "))
KM = 1.60934 * v
MI = 1.60934 / v
if (u.upper() == "K"):
	print(round(MI, 2))
if (u.upper() == "M"):
	print(round(KM, 2))