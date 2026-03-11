from numpy import *
vetor = array(eval(input()))

saida=0
for i in range(len(vetor)):
    saida= saida+vetor[i]*(i+1)

print(saida)