uni = input("unidade de medida em M (milha) ou K (quilometro): ").upper()
val = float(input("valor da medida: "))

if uni == "M":
	km = 1.60934*val
	print(round(km,2))
else:
	m = val/1.60934
	print(round(m,2))