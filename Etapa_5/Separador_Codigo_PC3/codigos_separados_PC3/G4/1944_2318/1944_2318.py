aminoacido= input("nome do aminoacido")
aminoacido=aminoacido.upper()
O=15.9994
C=12.011
N=14.00674
H=1.0079
if aminoacido== "LEUCINA":
	print(round((C*6+H*13+N+O*2),2))
	
else:
	print(round((C*6+H*15+N*2+O*2),2))