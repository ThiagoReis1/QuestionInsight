from numpy import*
cor=input("cor dos olhos: ").split(",")

vet=zeros(5,dtype=int)
for i in cor:
	if(i=="P"):
		vet[0]=vet[0]+1
	elif(i=="C"):
		vet[1]=vet[1]+1
	elif(i=="M"):
		vet[2]=vet[2]+1
	elif(i=="V"):
		vet[3]=vet[3]+1
	elif(i=="A"):
		vet[4]=vet[4]+1
		
print(max(vet))
print(vet)