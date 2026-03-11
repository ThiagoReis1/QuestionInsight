from numpy import*

n=input().upper(). split(",")

vetor = zeros(4,dtype = int)

for i in range (size(n)):
	if n[i] == 'A':
		vetor[0]= vetor[0]+1
	elif n[i] == 'B':
		vetor[1]= vetor[1] + 1
	elif n[i]== 'C':
		vetor[2]= vetor[2] + 1
	elif n[i] == 'D':
		vetor[3]= vetor[3] + 1
print(vetor)