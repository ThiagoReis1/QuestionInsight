n1= input("nome do aminoacido: ")
O=15.9994
C=12.011
N=14.00674
H=1.00794
if(n1.upper()=="ARGININA"):
	peso=(C*6)+(H*15)+(N*4)+(O*2)
	print(round(peso,2))
if(n1.upper()=="TIROSINA"):
	peso=(C*9)+(H*11)+N+(O*3)
	print(round(peso,2))