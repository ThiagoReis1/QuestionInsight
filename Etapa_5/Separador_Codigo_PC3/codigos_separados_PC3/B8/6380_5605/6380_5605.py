from numpy import*
contadores =zeros(4, dtype=int)

vet= input("").upper().split(',')

for i in range (0 , size(vet)):
	if vet[i] == "E":
		contadores[0]=contadores[0]+1
	elif vet[i]== "V":
		contadores[1]=contadores[1]+1
	elif vet[i] == "A":
		contadores[2]= contadores[2]+1
	elif vet[i] == "D":
		contadores[3]= contadores[3]+1
		
print(contadores)