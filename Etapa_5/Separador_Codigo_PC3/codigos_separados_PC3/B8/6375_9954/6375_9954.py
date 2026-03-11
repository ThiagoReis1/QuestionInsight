from numpy import*

vetor = zeros(4, dtype = int)
contagem = input().upper().split(',')

for i in range(0, size(contagem), 1):
	if contagem[i] == "A":
		vetor[0] = vetor[0] + 1
	elif contagem[i] == "B":
		vetor[1] = vetor[1] + 1
	elif contagem[i] == "C":
		vetor[2] = vetor[2] + 1
	elif contagem[i] == "D":
		vetor[3] = vetor[3] + 1
		
print(vetor)