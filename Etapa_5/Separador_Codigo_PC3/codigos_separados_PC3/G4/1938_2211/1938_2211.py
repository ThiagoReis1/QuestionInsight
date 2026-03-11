O=15.9994
C=12.011
N=14.00674
H=1.00794
ARGININA=(C*6)+(H*15)+(N*4)+(O*2)
TIROSINA=(C*9)+(H*11)+(N+(O*3))

nome= input("tipo de aminoacido: ")

if (nome=="ARGININA"):
    peso=ARGININA
else:
	 peso=TIROSINA
print (round(peso,2))