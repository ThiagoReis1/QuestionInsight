aminoacido=input("Digite o aminoacido: ").upper()

O=15.9994
C=12.011
N=14.0067
H=1.00794
formula=0

if(aminoacido=="GLUTAMINA"):
	formula=C*5+H*8+N*1+O*4
	print(round(formula,2))
elif(aminoacido=="SERINA"):
	formula=C*3+H*7+N*1+O*3
	print(round(formula,2))
elif(aminoacido=="TREONINA"):
	fomula=C*4+H*9+N*1+O*3
	print(round(formula,2))
else:
	print("Entrada:", aminoacido)
	print("Dado Invalido")
