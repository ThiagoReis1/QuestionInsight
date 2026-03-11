u = input("Unidade de medida(K/M): ").upper()
v = float(input("Valor da medida: "))
if (u == "M"):
	t = 1.60934 * v
else:
	t = v/1.60934
print(round(t,2))
