from numpy import*
strin=input("asas: ").upper().split(',')

vet=zeros(5,dtype=int)

for i in range(size(strin)):
	if (strin[i] == "AM"):
		vet[0] = vet[0] + 1
	elif (strin[i] == "PE"):
		vet[1] = vet[1] + 1
	elif (strin[i] == "MG"):
		vet[2] = vet[2] + 1
	elif (strin[i] == "SP"):
		vet[3] = vet[3] + 1
	elif(strin[i] =="RS"):
		vet[4] = vet[4] + 1
print(max(vet))
print(vet)
