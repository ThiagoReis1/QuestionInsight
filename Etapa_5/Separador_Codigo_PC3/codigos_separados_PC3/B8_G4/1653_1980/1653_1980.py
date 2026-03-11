from numpy import*

ent = input("")
vet = ent .split(',')
vet1 = zeros(5, dtype=int)

for i in range(size(vet)):
	if(vet[i] == "AR"):
		vet1[0] += 1
	elif(vet[i] == "BR"):
		vet1[1] += 1
	elif(vet[i] == "CL"):
		vet1[2] += 1
	elif(vet[i] == "CO"):
		vet1[3] += 1
	elif(vet[i] == "UY"):
		vet1[4] += 1
		
print(max(vet1))
print(vet1)