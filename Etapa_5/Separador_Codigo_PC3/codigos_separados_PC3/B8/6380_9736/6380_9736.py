from numpy import*

vetor = zeros(4, dtype = int)
estoque = input().upper().split(',')

for i in range(0, size(estoque),1):
	
	if estoque[i] == "E":
		vetor[0] = vetor[0] + 1
	
	elif estoque[i] == "V":
		vetor[1] = vetor[1] + 1
	
	elif estoque[i] == "A":
		vetor[2] = vetor[2] + 1

	elif estoque[i] == "D":
		vetor[3] = vetor[3] + 1
		
print(vetor)