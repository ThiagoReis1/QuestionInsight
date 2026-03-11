c = float(input("Consumo de minutos: "))
if c <= 100:
	h = c*1.2
	print(round(h,2))
else:
	g = 25 + (1.4*c)
	print(round(g,2))