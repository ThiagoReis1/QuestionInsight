from numpy import *

l=input("qnt.:").split(',')
vet=zeros(5,dtype=int)

for i in l:
	if(i=="AZ"):
		vet[0] +=1
	elif(i=="CA"):
		vet[1] +=1
	elif(i=="FL"):
		vet[2] +=1
	elif(i=="PA"):
		vet[3] +=1
	elif(i=="WI"):
		vet[4] +=1
		
print(max(vet))
print(vet)