from math import *
numx=eval(input("Digite o numero real x:"))
numk=int(input("Digite um  numero inteiro k:"))
i=0
kf=0
j=0

while(i<numk):
	ak=((numx**j)/factorial(j))
	kf=kf+ak
	j=j+1
	i=i+1
print(round(kf,9))