#---------------------------------------------------------
# UNIVERSIDADE FEDERAL DO AMAZONAS
# ANA REBECA CAVALCANTE EVANGELISTA 
# MATRICULA: 21456290
# DATA: 25/08/2016
# AVALIAÇÃO PARCIAL 06
#---------------------------------------------------------

from numpy import *

vetor = array(eval(input("Digite os valores do vetor: ")))

A = min(vetor)
B = max(vetor)

x1 = 0 
x2 = 0

total = zeros(2, dtype=int)

C = 0.65 * A + 0.35 * B
D = 0.45 * A + 0.55 * B

for i in range(0, size(vetor)):
	if vetor[i] >= A and vetor[i] < C :
		x1 = x1 + 1
	if vetor[i] >= C and vetor[i] < D :
		x2 = x2 + 1

total[0] = x1
total[1] = x2

print(total)
	