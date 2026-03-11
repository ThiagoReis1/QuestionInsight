O=15.9994
C=12.011
N=14.0067
S=32.066
H=1.00794


A=input("digite o nome do amino: ")

if A.lower() == "aspartato":
	aminoacido=C*4+H*6+N+O*4

else:
	aminoacido=C*3+H*7+N+O*2+S
print(round(aminoacido,2))
