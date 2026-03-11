from numpy import*
from math import*

vetor = array(eval(input("digite o vetor: ")))
saida = array(zeros(2, dtype = int))

A = min(vetor)
B = max(vetor)
C = 0.75* A + 0.25* B
D = 0.25* A + 0.75* B
con = 0
for i in range(size(vetor)):
	if((vetor[i]>= A) and (vetor[i] < C)):
		saida[0] = saida[0] + 1
for i in range(size(vetor)):		
	if((vetor[i] >= D) and (vetor[i] < B)):
		saida[1] = saida[1] + 1
		
print(saida)