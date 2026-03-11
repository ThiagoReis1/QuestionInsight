from numpy import*

vetor = zeros(4, dtype = int)
nota = input().upper().split(',')

for i in range(size(nota)):
	if nota[i] == "C":
		vetor[0] = vetor[0] + 1
	elif nota[i] == "D":
		vetor[1] = vetor[1] + 1
	elif nota[i] == "V":
		vetor[2] = vetor[2] + 1
	elif nota[i] == "U":
		vetor[3] = vetor[3] + 1
print(vetor)