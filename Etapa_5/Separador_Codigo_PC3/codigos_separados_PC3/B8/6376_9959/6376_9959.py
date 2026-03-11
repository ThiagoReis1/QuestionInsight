from numpy import * 

x = input().split(',')
vetor = zeros(4, dtype=int)
j = size(x)

for i in range (j):
	if x[i] == 'A':
		vetor[0] += 1
	elif x[i] == 'B':
		vetor[1] += 1
	elif x[i] == 'C':
		vetor[2] += 1
	elif x[i] == 'D':
		vetor[3] += 1
		
print(vetor)