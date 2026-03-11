aminoacido= input("Digite o aminoacido: ").upper()

O= float(15.9994)
C= float(12.011)
N= float(14.00674)
H= float(1.00794)

argininab= float((C * 6) + (H * 15) + (N * 4) + (O * 2))
tirosinab= float((C * 9) + (H * 11) + (N * 1) + (O * 3))

if (aminoacido == "ARGININA") :
	print(round(argininab, 2))
else:
	print(round(tirosinab, 2))
