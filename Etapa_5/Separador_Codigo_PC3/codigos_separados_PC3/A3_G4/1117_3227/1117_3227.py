p = float(input())
d = int(input())
m = input("s ou n").upper()
ds = (p * 0.25)
print("Entradas: ", p, ",", d, ",", m)

if ((p >= 0) and (1 <= d <= 7) and ((m == "S") or (m == "N"))):
	if ((d == 2) or (d ==3) or (d == 5) and (m == "N")):
		pt = p - ds
	if (m == "S"):
		pt = (p - ds) + 20.00
		print("Valor a pagar: R$", round(pt, 2))
else:
	print("Dados invalidos")