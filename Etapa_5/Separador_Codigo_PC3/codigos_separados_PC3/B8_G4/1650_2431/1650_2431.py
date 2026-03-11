from numpy import *

ent = input("")
vet = ent .split(',')
vet1 = zeros(5, dtype=int)

for i in range(size(vet)):
	if(vet[i] == "P"):
		vet1[0] += 1
	elif(vet[i] == "C"):
		vet1[1] += 1
	elif(vet[i] == "R"):
		vet1[2] += 1
	elif(vet[i] == "L"):
		vet1[3] += 1
	elif(vet[i] == "B"):
		vet1[4] +=1
	
print(max(vet1))
print(vet1)