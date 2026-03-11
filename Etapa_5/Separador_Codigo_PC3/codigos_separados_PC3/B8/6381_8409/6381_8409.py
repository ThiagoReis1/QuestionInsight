from numpy import*
cartas = input("cartas:").upper().split(",")
vetor = zeros(4,dtype = int)
for i in range(size(cartas)):
	if cartas[i] == "C":
		vetor[0] = vetor[0] + 1
	elif cartas[i] == "O":
		vetor[1] = vetor[1] + 1
	elif cartas[i] == "P":
		vetor[2] = vetor[2] + 1 
	elif cartas[i] == "E":
		vetor[3] = vetor[3] + 1

print(vetor)