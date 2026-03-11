from numpy import*

paises=input("ASAS: ").split(',')
vet=zeros(5,dtype=int)
for i in paises:
	if(i == "AC"):
		vet[0]=vet[0]+1
	elif(i == "AM"):
		vet[1]=vet[1]+1
	elif(i == "PA"):
		vet[2]=vet[2]+1
	elif(i == "RO"):
		vet[3]=vet[3]+1
	elif(i == "RR"):
		vet[4]=vet[4]+1
print(max(vet))
print(vet)
