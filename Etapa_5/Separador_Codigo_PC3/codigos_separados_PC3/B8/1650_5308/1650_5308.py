from numpy import*
cabelos = input("").split(',')

vet = zeros(5,dtype=int)

for i in range(len(cabelos)):
	if cabelos[i] == "P":
		vet[0] = vet[0] + 1
		
	elif cabelos[i] == "C":
		vet[1] = vet[1] + 1
		
	elif cabelos[i] == "R":
		vet[2] = vet[2] + 1
		
	elif cabelos[i] == "L":
		vet[3] = vet[3] + 1
		
	elif cabelos[i] == "B":
		vet[4] = vet[4] + 1
		
print(max(vet))
print(vet)