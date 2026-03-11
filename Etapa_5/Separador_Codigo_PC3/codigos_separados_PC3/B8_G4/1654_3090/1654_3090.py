from numpy import * 
m = input("Estados:").split(',')
vet = zeros(5, dtype=int)
for i in m:
	if(m == "AM"):
		vet[0] = vet [0]+1
	elif(m == "PE"):
		vet[1] = vet [1]+1
	elif(m == "MG"):
		vet[2] = vet [2]+1
	elif(m == "SP"):
		vet[3] = vet [3]+1
	elif(m == "RS"):
		vet[4] = vet [4]+1
print(vet)		
	