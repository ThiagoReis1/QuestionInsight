aminoacido = input("nome do aminoacido:")
aminoacido = aminoacido.upper()
O = 15.9994
C = 12.011
N = 14.00674
H = 1.00794
if (aminoacido == "ARGININA"):
	VALOR = C*6+H*15+N*4+O*2
	print(round(VALOR,2))
else:
	print(round(C*9+H*11+N+O*3,2))
	