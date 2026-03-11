from numpy import*

x=input("digite os estados: ").split(',')

vet=zeros(5,dtype= int)

for elemento in x:
	if (elemento== 'AM'):
		vet[0]+=1
	if (elemento== 'PE'):
		vet[1]+=1
	if (elemento== 'MG'):
		vet[2]+=1
	if (elemento== 'SP'):
		vet[3]+=1
	if (elemento== 'RS'):
		vet[4]+=1
		
print(max(vet))
print(vet)
	