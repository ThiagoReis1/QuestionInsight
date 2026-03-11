
aminoacido=input().lower()
O= 15.9994
C= 12.011
N= 14.0067
S= 32.066
H= 1.00794
if aminoacido== "aspartato":
	formula= C*4+H*6+N+O*4
	print(round(formula,2))
	
elif aminoacido== "cisteina":
	formula= C*3+H*7+N+O*2+S
	print(round(formula,2))
	
elif aminoacido== "metionina":
	formula = C*5+H*11+N+O*2+S
	print(round(formula,2))
else:
	print("Entrada:",aminoacido)
	print("Dado Invalido")
	