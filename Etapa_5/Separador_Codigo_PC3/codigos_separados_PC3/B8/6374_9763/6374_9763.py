from numpy import*
vetor = zeros(4, dtype = int)
livro = input().upper().split(',')

for i in range(size(livro)):
	if livro[i] == "O":
		vetor[0] = vetor[0] + 1
	elif livro[i] == "D":
		vetor[1] = vetor[1] + 1
	elif livro[i] == "N":
		vetor[2] = vetor[2] + 1
	elif livro[i] == "C":
		vetor[3] = vetor[3] + 1
		
print(vetor)