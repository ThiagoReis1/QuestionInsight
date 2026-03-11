letra = input("letra tal: ").upper()
valorm = float(input("valor da medida: "))

if letra == "K":
	K = valorm * 2.35215
	print(round(K, 2))
else: 
	M = valorm / 2.35215
	print(round(M, 2))