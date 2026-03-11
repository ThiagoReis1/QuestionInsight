p = float(input("Preco: "))
d = int(input("dia: "))
m = input("Musica (s ou n)").upper()
ds = (p * 0.25)
tx = 20.00

print("Entradas: ", p, ",", d, ",", m)

if ((p >= 0) and (1 <= d <= 7) and ((m == "S") or (m == "N"))):
	if (((d == 2) or (d == 3) or (d == 5)) and (m == "N")):
		pt = p - ds
	elif ((d == 2) or (d == 3) or (d == 5) and (m == "S")):
		pt = (p - ds) + tx
	elif (((d == 1) or (d == 4) or (d == 6) or (d == 7)) and (m == "N")):
		pt = p
	elif (((d == 1) or (d == 4) or (d == 6) or (d == 7)) and (m == "S")):
		pt = p + tx
	print("Valor a pagar: R$", round(pt, 2))
else:
	print("Dados invalidos")