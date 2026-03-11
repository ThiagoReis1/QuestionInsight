#Universidade Federal do Amazonas
#Thiago Tuma Camilo 21600549
from numpy import *
vetor = array(eval(input("Digite um vetor:")))
A = min(vetor)
B = max(vetor)
C = (0.65 * A) + (0.35 * B)
D = (0.45 * A) + (0.55 * B)
x = array(zeros(2, dtype = int))
for i in range(size(vetor)):
	if (vetor[i] >= A) and (vetor[i] < C):
		x[0] = x[0] + 1
	elif (vetor[i] >= C) and (vetor[i] < D):
		x[1] = x[1] + 1
print(x)