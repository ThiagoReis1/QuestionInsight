
C=12.011
O=15.9994
N=14.00674
H=1.0079

nom=input("digite o nome: ")
if nom.lower() == "leucina":
	aminoacido=((C*6)+(H*13)+(N)+(O*2))
else:
	aminoacido=((C*6)+(H*15)+(N*2)+(O*2))
	
print(round(aminoacido,2))