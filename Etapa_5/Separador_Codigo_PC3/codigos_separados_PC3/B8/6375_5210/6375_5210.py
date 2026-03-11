x = input("")
from numpy import*
j = x.split(",")

vetor = zeros(4, dtype = int)

for s in j:
	if s=='A':
		vetor[0] = vetor[0] + 1
	elif s =='B':
		vetor[1] = vetor[1] + 1
	elif s =='C':
		vetor[2] = vetor[2] + 1
	elif s =='D':
		vetor[3] = vetor[3] +1
print(vetor)