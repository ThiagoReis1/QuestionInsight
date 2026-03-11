comida = input("L/P: ")
ql = int(input("quantidade de lanches: "))
qr = int(input("quantidade de refrigerantes"))

if (comida == "L"):
	print(round(ql * 6.0 + 3.0 * qr,1))
else:
	print(round(ql * 13.50 + 3.0 * qr,1))
	
	
