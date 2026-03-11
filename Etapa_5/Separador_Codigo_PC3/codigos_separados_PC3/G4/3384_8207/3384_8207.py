k = input(" (O) para oncas ou (K) para quilogramas")
if k=="K":
	k1= float(input("k"))
	oo= 35.274 * k1
	print(round(oo, 2))
else:
	o_1=float(input("o"))
	k2 = o_1 / 35.274
	print(round(k2, 2))