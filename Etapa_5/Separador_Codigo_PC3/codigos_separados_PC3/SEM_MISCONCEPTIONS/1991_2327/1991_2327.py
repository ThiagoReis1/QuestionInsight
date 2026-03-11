
aminoacido= input().upper()
O= 15.9994
C= 12.011
N= 14.00674
H= 1.0079
if aminoacido== "GLICINA":
	formula= C*2+H*5+N+O*2
	print(round(formula,2))
elif aminoacido== "PROLINA":
	formula= C*5+H*10+N+O*2
	print(round(formula,2))
elif aminoacido== "SERINA":
	formula= C*3+H*7+N+O*3
	print(round(formula,2))
else:
	print("Entrada:",aminoacido)
	print("Dado Invalido")
	 