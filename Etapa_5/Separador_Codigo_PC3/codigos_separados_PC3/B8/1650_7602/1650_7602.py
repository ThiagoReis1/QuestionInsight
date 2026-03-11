from numpy import*

cabelo = input().upper().split(',')

vet = zeros(5,dtype=int)

for i in range(len(cabelo)):
	if cabelo[i] =="P":
		vet[0] += 1
	elif cabelo[i] =="C":
		vet[1] +=1
	elif cabelo[i] =="R":
		vet[2] += 1
	elif cabelo[i] == "L":
		vet[3] += 1
	elif cabelo[i] == "B":
		vet[4] += 1
		
print(max(vet))
print(vet)
	