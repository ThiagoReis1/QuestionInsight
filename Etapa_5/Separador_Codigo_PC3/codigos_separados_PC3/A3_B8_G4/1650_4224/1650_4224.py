from numpy import*
from numpy.linalg import*
s=input("")
v=s.split(",")
vet=zeros(5,dtype=int)

cont=0
a=0
b=0
for i in range(size(v)):
	if(v[i]=="P"):
		vet[0]=vet[0]+1
	elif(v[i]=="C"):
		vet[1]=vet[1]+1
	elif(v[i]=="R"):
		vet[2]=vet[2]+1
	elif(v[i]=="L"):
		vet[3]=vet[3]+1
	elif(v[i]=="B"):
		vet[4]=vet[4]+1
print(max(vet))
print(vet)



