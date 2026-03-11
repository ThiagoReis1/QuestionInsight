from numpy import *
 
cont= zeros(5, dtype=int)
vet= input().upper().slpit(",")
for i in range(size(vet)):
	if (vet[i]=="CA"):
		cont[0]= cont[0] + 1
	elif(vet[i]=="AZ"):
		cont[1]=cont[1] + 1
	elif(vet[i]=="FL"):
		cont[2]=cont[2] + 1
	elif(vet[i]=="WI"):
		cont[3]=cont[3] + 1
	elif(vet[i]=="CA"):
		cont[4]=cont[4] + 1
	elif(vet[i]=="PA"):
		cont[5]=cont[5] + 1	
print(max(cont))
print(cont)
	 