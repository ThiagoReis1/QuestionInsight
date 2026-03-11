from numpy import*

pes= input("maior: ").split(',')

vet=zeros(5,dtype = int)
for i in pes:
	if(i=="BE"):
		vet[0]=vet[0]+1
	elif(i=="ES"):
		vet[1]=vet[1]+1
	elif(i=="FR"):
		vet[2]=vet[2]+1
	elif(i=="IT"):
		vet[3]=vet[3]+1
	elif(i=="PT"):
		vet[4]=vet[4]+1
print(max(vet))
print(vet)