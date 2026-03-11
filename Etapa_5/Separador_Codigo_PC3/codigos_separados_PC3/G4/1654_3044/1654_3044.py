from numpy import*
vet=input("cidades:").split(",")
i=0
z=zeros(5,dtype=int)
while(i<size(vet)):
	if(vet[i]=="AM"):
		z[0]=z[0]+1
	if(vet[i]=="PE"):
		z[1]=z[1]+1
	if(vet[i]=="MG"):
		z[2]=z[2]+1
	if(vet[i]=="SP"):
		z[3]=z[3]+1
	if(vet[i]=="RS"):
		z[4]=z[4]+1
	i=i+1
print(max(z))
print(z)