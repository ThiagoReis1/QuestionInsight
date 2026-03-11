from numpy import *	
x = input("x:")
vet = zeros(5,dtype=int)
x = x.split(',')
a = 0

for i in range(size(x)):
	if(x[i]=="P"):
		vet[0]=vet[0] + 1
	elif(x[i]=="C"):
		vet[1]=vet[1]+ 1
	elif(x[i]=="R"):
		vet[2]=vet[2] + 1
	elif(x[i]=="L"):
		vet[3]=vet[3] + 1
	elif(x[i]=="B"):
		vet[4]=vet[4] + 1
	
print(max(vet))
print(vet)