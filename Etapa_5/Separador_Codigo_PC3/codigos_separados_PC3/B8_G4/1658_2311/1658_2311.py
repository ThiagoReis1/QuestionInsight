from numpy import *
ent = input("")
vet = ent .split(",")
vet1 = zeros(5, dtype=int)

for i in range(size(vet)):
	if(vet[i] == "CHN"):
		vet1[0] += 1
	elif(vet[i] == "JPN"):
		vet1[1] += 1
	elif(vet[i] == "KOR"):
		vet1[2] += 1
	elif(vet[i] == "MGL"):
		vet1[3] += 1
	elif(vet[i] == "THA"):
		vet1[4] += 1

print(max(vet1))
print(vet1)