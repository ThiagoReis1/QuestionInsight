x=input("Peso da (Arginina/Tirosina/Triptofano): ")
O= 15.9994
C= 12.011
N= 14.00674
H= 1.00794
Arg=(C*6)+(H*15)+(N*4)+(O*2)
Tir=(C*9)+(H*11)+N+(O*3)
Tri=(C*11)+(H*11)+(N*2)+(O*2)
if (x.upper()!="ARGININA") and (x.upper()!="TIROSINA" ) and (x.upper()!="TRIPTOFANO" ):
	print("Entrada: ", x.upper())
	print("Dado Invalido")
else:
	if x.upper()=="ARGININA":
		print(round(Arg,2))
	elif x.upper()=="TIROSINA":
		print(round(Tir,2))
	else:
		print(round(Tri,2))