from numpy import*
cartas = input("cartas: ").upper().split(',')

vet= zeros(4, dtype = int)

for i in range(size(cartas)):
	if cartas[i] == "C":
		vet[0]= vet[0]+1
	elif cartas[i] == "O":
		vet[1]= vet[1]+1
	elif cartas[i] =="P":
		vet[2]= vet[2]+1
	elif cartas[i] == "E":
		vet[3] = vet[3]+1
		
print(vet)

