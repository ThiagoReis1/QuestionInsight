
aminoacido=input().lower()
O=15.999
C=12.011
N=14.00674
H=1.00794

if aminoacido== "glutamina":
	formula=C*3+H*8+N*1+O*4
	print(round(formula,2))
elif aminoacido== "histidina":
	formula=C*6+H*10+N*3+O*2
	print(round(formula,2))
elif aminoacido== "prolina":
	formula=C*5+H*10+NO*2
	print(round(formula,2))
else :
	print("Entrada:",aminoacido)
	print("Dado Invalido")
	
