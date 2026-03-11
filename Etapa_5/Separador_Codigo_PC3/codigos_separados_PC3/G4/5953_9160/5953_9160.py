Ch = input("L ou P: ").upper()
Qt = float(input("Digite um numero: "))
Qr = float(input("Digite um numero: "))

if (Ch == "P"):
	P = Qt * 13.50 + Qr * 3
	print(round(P, 2))
	
else: 
	P = Qt * 6.00 + Qr * 3
	print(round(P, 2))
	