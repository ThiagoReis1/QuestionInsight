nda = input("insira seu aminoácido aqui: ").upper()

O = 15.999
C = 12.011
N = 14.00674
H = 1.00794

Asp = (C*4 + H*8 + N*2 + O*3)
Tri = (C*11 + H*11 + N*2 + O*2)

if (nda == "ASPARAGINA"):
	print(round(Asp,2))
else:
	print(round(Tri,2))












