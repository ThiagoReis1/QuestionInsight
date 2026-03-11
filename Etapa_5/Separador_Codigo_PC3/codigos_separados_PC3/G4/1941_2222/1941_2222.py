
nome=input("aminoacido: ".upper())
O=15.9994
C=12.011
N=14.00674
H=1.0079

if(nome.upper()=="GLICINA"):
	PESO=(C*2)+(H*5)+(N*1)+(O*2)
else:
	PESO=(C*3)+(H*7)+(N*1)+(O*3)
	
print(round(PESO, 2))