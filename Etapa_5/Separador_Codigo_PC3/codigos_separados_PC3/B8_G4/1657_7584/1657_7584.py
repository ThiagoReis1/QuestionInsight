from numpy import *

pais = input("Estados: ").upper().split(',')

i = 0

vet = zeros(5 , dtype = int)

for i in range(size(pais)):
	if(pais[i] == "AZ"):
		vet[0] += 1 
	elif(pais[i] == "CA"):
		vet[1] += 1 
	elif(pais[i] == "FL"):
		vet[2] += 1
	elif(pais[i] == "PA"):
		vet[3] += 1
	elif(pais[i] == "WI"):
		vet[4] += 1
print(max(vet))
print(vet)