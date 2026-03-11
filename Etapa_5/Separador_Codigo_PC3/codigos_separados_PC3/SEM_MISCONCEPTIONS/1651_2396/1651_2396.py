from numpy import *

v=input().split(',')
cont=0
vet=zeros(6,dtype=int)

for i in range(size(v)):
	if(v[i]=="MC"):
		vet[0]=vet[0]+1
	elif(v[i]=="C"):
		vet[1]=vet[1]+1
	elif(v[i]=="CM"):55555
		vet[2]=vet[2]+1
	elif(v[i]=="EM"):
		vet[3]=vet[3]+1
	elif(v[i]=="E"):
		vet[4]=vet[4]+1
	elif(v[i]=="ME"):
		vet[5]=vet[5]+1

		
print(max(vet))
print(vet)


	