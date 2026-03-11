ra = input("unidade de medida: ")
ra2 = float(input("valor da medida: "))

if (ra.upper() == "K"):
	b = 2.20462*ra2
else:
	b = ra2/2.20462

print(round(b, 2))