# Paulo Bitencourt
# 25 - 08 - 2016

from numpy import*
from math import*

vetor = array(eval(input("Vetor: ")))

saida = array(zeros(2 , dtype = int))

A = min(vetor)
B = max(vetor)
C = 0.65 * A + 0.35 * B
D = 0.45 * A + 0.55 * B

for i in range(size(vetor)):
	if (vetor[i] >= A and vetor[i] < C):
		saida[0] = saida[0] + 1
		
for i in range(size(vetor)):
	if (vetor[i] >= C and  vetor[i] < D):
		saida[1] = saida [1] + 1
print(saida)