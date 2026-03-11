
aminoacido=input().upper()
O=15.999
C=12.011
N=14.00674
H=1.00794
if aminoacido=="ASPARAGINA":
	formula=C*4+H*8+N*2+O*3
	print(round(formula,2))
elif aminoacido=="GLUTAMINA":
	formula=C*5+H*8+N*1+O*4
	print(round(formula,2))
elif aminoacido=="TRIPTOFANO":
	formula =C*11+H*11+N*2+O*2
	print(round(formula,2))
else:
	print("Entrada:",aminoacido)
	print("Dado Invalido")