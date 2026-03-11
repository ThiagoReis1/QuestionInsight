aminoacido=input().upper()
C = 12.011
H = 1.00794
N = 14.00674
O = 15.9994

if aminoacido=="ALANINA":
		formula= C*3+H*7+N+O*2
		print(round(formula,2))
elif aminoacido=="VALINA":
		formula= C*5+H*11+N+O*2
		print(round(formula,2))
elif aminoacido=="TIROSINA":
		formula= C*9+H*11+N+O*3
		print(round(formula,2))
else:
	print("Entrada:",aminoacido)
	print("Dado Invalido")