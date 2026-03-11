Nm = float(input("digite o numero de mangas: "))

if Nm < 6:
	Vt = Nm * 3.80
	print(round(Vt,2))
else:
	Vt = Nm * 3.45
	print(round(Vt,2))