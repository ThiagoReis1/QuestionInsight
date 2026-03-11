from numpy import *
s = input("s:")
vet = s.split(',')

vc = zeros(5, dtype=int)

for i in range(0,size(vet)):
	if(vet[i]=='B'):
		vc[0]=vc[0]+1
	elif(vet[i]=='PA'):
		vc[1]=vc[1]+1
	elif(vet[i]=='PR'):
		vc[2]=vc[2]+1
	elif(vet[i]=='A'):
		vc[3]=vc[3]+1
	elif(vet[i]=='I'):
		vc[4]=vc[4]+1
print(max(vc))
print(vc)

