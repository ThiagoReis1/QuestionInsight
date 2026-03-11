from numpy import*
vet1 = input("estados").upper().split(',')
i = 0 

vet =zeros(5,dtype = int)

for i in range(size(vet1)):
	if(vet1[i] == "AM"):
		vet[0] = vet[0] + 1
	elif(vet1[i]=="PE"):
		vet[1] = vet[1]+1
	elif(vet1[i]=="MG"):
		vet[2] = vet[2] +1
	elif(vet1[i]=="SP"):
		vet[3]=vet[3]+1
	elif(vet1[i]=="RS"):
		vet[4]=vet[4]+1
print(max(vet))
print(vet)
	
	


	
	
	
	
	
	
