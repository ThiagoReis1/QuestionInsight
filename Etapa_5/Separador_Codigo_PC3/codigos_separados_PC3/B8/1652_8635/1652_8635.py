from numpy import*
texto = input("").upper().split(",")
i = 0
vetor = zeros(5,dtype=int)

while i < len(texto):
	if texto[i] == "B":
		vetor[0] = vetor[0] + 1
	elif texto[i] == "PA":
		vetor[1] = vetor[1] + 1
	elif texto[i] == "PR":
		vetor[2] = vetor[2] + 1
	elif texto[i] == "A":
		vetor[3] = vetor[3] + 1
	elif texto[i] == "I":
		vetor[4] = vetor[4] + 1
	i = i + 1
print(max(vetor))
print(vetor)


