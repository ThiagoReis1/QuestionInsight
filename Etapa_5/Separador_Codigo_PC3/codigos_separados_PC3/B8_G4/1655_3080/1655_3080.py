from numpy import *
s= input().split(',')
vet = zeros(5, dtype=int)
for i in range(size(s)):
	if(s[i] == "AC"):
		vet[0]= vet[0] + 1
	elif(s[i] == "AM"):
		vet[1] == vet[1] + 1
	elif(s[i] == "PA"):
		vet[2]= vet[2] + 1
	elif(s[i]== "RO"):
		vet[3] == vet[3] + 1
	elif(s[i] == "RR"):
		vet[4] == vet[4] + 1
print(max(vet))
print(vet)


