aminoacido= input("nome do aminoacido")
aminoacido=aminoacido.upper()
O=15.9994
C=12.011
N=14.00674
H=1.0079
if aminoacido=="GLICINA":
	print(round((C*2+H*5+N+O*2),2))
			
if aminoacido== "SERINA":
	print(round((C*3+H*7+N+O*3),2))
	