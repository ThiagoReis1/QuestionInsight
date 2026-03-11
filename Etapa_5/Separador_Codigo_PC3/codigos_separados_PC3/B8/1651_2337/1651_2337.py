from numpy import*

string = input()
vet = string.split(',')
vet1 = zeros(6,dtype=int)

for i in range(size(vet)):
	if(vet[i] == "MC"):
		vet1[0] += 1
	elif(vet[i] == "C"):
		vet1[1] += 1
	elif(vet[i] == "CM"):
		vet1[2] += 1
	elif(vet[i] == "EM"):
		vet1[3] += 1
	elif(vet[i] == "E"):
		vet1[4] += 1
	elif(vet[i] == "ME"):
		vet1[5] += 1
		
print(max(vet1))
print(vet1)
