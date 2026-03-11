from numpy import*

vetor = zeros(4, dtype = int)
notas = input().upper().split(',')

for i in range(0, size(notas), 1):
	if notas[i] == "C":
		vetor[0] = vetor[0] + 1
	elif notas[i] == "D":
		vetor[1] = vetor[1] + 1
	elif notas[i] == "V":
		vetor[2] = vetor[2] + 1
	elif notas[i] == "U":
		vetor[3] = vetor[3] + 1
		
print(vetor)