u = input("unidade de medida: ").upper()
v = float(input("valor da medida: "))

if (u == "K"):
	t = 2.35215 * v

else:
	t = v / 2.35215

print(round(t, 2))