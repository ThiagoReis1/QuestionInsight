C=12.011
O=15.9994
N=14.00674
H=1.00794
A=input("digite o aminoacido: ")

if A.upper() == "ARGININA":
	aminoacido=((C*6)+(H*15)+(N*4)+(O*2))
else:
	aminoacido=((C*9)+(H*11)+(N*1)+(O*3))
print(round(aminoacido,2))
