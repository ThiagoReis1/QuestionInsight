
aminoacido=aminoacido.lower()
O=15.999
C=12.011
N=14.00674
S=32.066
H=1.00794
if aminoacido=="aspartato":
	formula= C*4+H*6+N*1+O*4
	print(round(formula,2))
elif aminoacido=="fenilalanina":
	formula= C*9+H*11+O*2+S*1
	print(round(formula,2))
elif aminoacido=="tirosina":
   formula= C*9+ H*11+ N*1+O*3
	print(round(formula,2))
else:
	print("Entrada:", aminoacido)
	print("Dado invalido")
	
	