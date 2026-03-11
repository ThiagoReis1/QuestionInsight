from numpy import* 

v= input("Informe o estado de origem: ").upper().split(',')



vet=zeros(5,dtype=int)
s=0

for i in v:
	if(i=='AZ'):
		vet[0]=vet[0]+1
	elif(i=='CA'):
		vet[1]=vet[1]+1
	elif(i=='FL'):
		vet[2]=vet[2]+1
	elif(i=='PA'):
		vet[3]=vet[3]+1
	elif(i=='WI'):
		vet[4]=vet[4]+1

print(max(vet))		
print(vet)		