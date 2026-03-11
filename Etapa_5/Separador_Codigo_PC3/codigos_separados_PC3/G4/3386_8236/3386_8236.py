x = input("unidade de medida(R ou G): ")
y = float(input("valor do angulo: "))

if x == "R":
	G = y / 0.0174533
	print(round(G, 2))
else:
	R = 0.0174533 * y
	print(round(R, 2))