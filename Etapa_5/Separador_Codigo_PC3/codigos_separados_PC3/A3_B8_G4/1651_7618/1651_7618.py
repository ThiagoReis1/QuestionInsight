from numpy import *

cor=input("cor de pele : ").upper().split(',')

vet=zeros(6,dtype=int)
j=0
for i in range(size(cor)):
	if cor[i] == "MC":
		vet[0]= vet[0] + 1
	elif cor[i]== "C":
		vet[1]= vet[1] + 1
	elif cor[i]== "CM":
		vet[2]=vet[2] + 1
	elif cor[i] == "EM":
		vet[3]= vet[4]+ 1
	elif cor[i] == "E":
		vet[4]=s + 1 
	elif cor[i] == "ME":
		soma= soma+ 1
print(soma)


		
	