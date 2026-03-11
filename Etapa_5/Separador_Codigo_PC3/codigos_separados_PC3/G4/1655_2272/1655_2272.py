from numpy import*
vet=input("quantidade de pessoas:").upper().split(',')
cont=zeros(5,dtype=int)
for i in range(size(vet)):
	if(vet[i]=="AC"):
		cont[0]=cont[0] + 1
	if(vet[i]=="AM"):
		cont[1]=cont[1] + 1
	if(vet[i]=="PA"):
		cont[2]=cont[2] + 1
	if(vet[i]=="RO"):
		cont[3]=cont[3] + 1
	if(vet[i]=="RR"):
		cont[4]=cont[4] + 1
print(max(cont))
print(cont)