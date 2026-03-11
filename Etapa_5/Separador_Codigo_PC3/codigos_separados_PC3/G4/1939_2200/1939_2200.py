nome = input("nome do aminoacido: ")

O = 15.999
C = 12.011
N = 14.00674
H = 1.00794
Asparagina = C*4 + H*8 + N*2 + O*3
Triptofano = C*11 + H*11 + N*2 + O*2
if(nome.upper() == "ASPARAGINA"):
	print(round(Asparagina, 2))
else:
	print(round(Triptofano, 2))
