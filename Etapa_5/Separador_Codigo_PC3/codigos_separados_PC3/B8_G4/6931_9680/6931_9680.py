vl = float(input("valor da compra: "))
cp = input("forma de pagamento: ").upper()

v = vl-(vl*(18/100))
px = vl-(vl*(18/100))
c1 = vl
c2 = vl+(vl*(7/100))

if cp == "C":
	qt = input("quantas vezes: ")
	if qt == "1":
		print(round(c1, 2))
	elif qt == "2":
		print(round(c2, 2))
elif cp == "D":
	print(round(v, 2 ))
elif cp == "P":
	print(round(px, 2))
	