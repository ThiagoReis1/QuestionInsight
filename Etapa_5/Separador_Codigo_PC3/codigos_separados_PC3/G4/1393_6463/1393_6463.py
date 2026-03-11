pes = float(input("peso da encomenda: "))

if pes >= 5000:
	print(round(pes * 0.04 + 60, 2))
else:
	print(round(pes * 0.05,2))