from numpy import*

vetor = zeros(4,dtype = int)
pontos = input().upper().split(',')

for i in range(0, size(pontos),1):
	if pontos[i] == "A":
		vetor[0] = vetor[0] + 1
	elif pontos[i] == "B":
		vetor[1] = vetor[1] + 1
	elif pontos[i] == "C":
		vetor[2] = vetor[2] + 1
	elif pontos[i] == "D":
		vetor[3] = vetor[3] + 1
print(vetor)