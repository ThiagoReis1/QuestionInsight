from numpy import*
ent = input()
vet = ent . split(',')
vet1 = zeros(5, dtype=int)

for i in range(size(vet)):
	if(vet[i] == "P"):
		vet1[0] += 1
	elif(vet[i] == "C"):
		vet1[1] += 1
	elif(vet[i] == "M"):
		vet1[2] += 1
	elif(vet[i] == "V"):
		vet1[3] += 1
	elif(vet[i] == "A"):
		vet1[4] += 1
print(max(vet1))
print(vet1)