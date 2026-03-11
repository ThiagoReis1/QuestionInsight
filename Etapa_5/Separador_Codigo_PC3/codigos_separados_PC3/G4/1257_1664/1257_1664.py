#--------------------------------------------------------
# UNIVERSIDADE FEDERAL DO AMAZONAS	
# LARISSA SANTOS BRITO - 21454598
# DATA: 25/08/2016
# AVALIAÇÃO 06 - EXERCÍCIO 01
# OBJETIVO: Criar um vetor X de dois elementos inteiros
#--------------------------------------------------------
from numpy import *
 
v = array(eval(input("digite o vetor:")))
x1 = 0
x2= 0

A = min(v)
B = max(v)
vet = zeros(2, dtype=int)
C = 0.85 * A + 0.15 * B
D = 0.4 * A + 0.6 * B

for  i in range (size(v)):
	if (v[i] >= A and v[i]< C):
		x1 = x1 + 1
for i in range (size(v)):
	if (v[i] >= D and v[i] < B):
		x2 = x2 + 1
vet[0] = x1
vet[1] = x2

print(vet)

