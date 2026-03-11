nome= input("").upper()
O=15.9994
C=12.011
N= 14.00674
H= 1.00794

if (nome.upper() == "ALANINA"):
	Alanina=(C*3+H*7+N+O*2)
	print(round(Alanina,2))
elif (nome.upper() == "VALINA"):
	Valina = (C*5+H*11+N+O*2) 
	print(round(Valina,2))
elif(nome.upper() =="TIROSINA"):
	Tirosina=(C*9+H*11+N+O*3)
	print(round(Tirosina,2))
else:
	print("Entrada:",nome.upper())
	print("Dado Invalido")
	