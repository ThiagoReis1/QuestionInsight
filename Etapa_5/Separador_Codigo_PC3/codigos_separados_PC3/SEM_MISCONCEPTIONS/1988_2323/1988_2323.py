aminoacido=input().upper()
O= 15.9994
C= 12.011
N= 14.00674
H= 1.00794

if aminoacido== "ARGININA":
		formula= C*6+H*15+N*4+O*2
		print(round(formula,2))	
elif aminoacido== "TIROSINA":
		formula= C*9+H*11+N+O*3
		print(round(formula,2))
elif aminoacodo== "TRIPTOFANO":
		formula= C*11+H*11+N*2+O*2
		print(round(formula,2))
else:
	print("Entrada:",aminoacido)
	print("Dado Invalido")
	
	
