from math import*
from numpy import*
vetor = input("Evento Europeu:").split(',')
cont = zeros(5, dtype = int)
i = 0
for i in range(len(vetor)):
    if (vetor[i] == "BE"):
        cont[0] = cont[0] + 1
    elif (vetor[i] == "ES"):
        cont[1] = cont[1] + 1
    elif (vetor[i] == "FR"):
        cont[2] = cont[2] + 1
    elif (vetor[i] == "IT"):
        cont[3] = cont[3] + 1
    elif (vetor[i] == "PT"):
        cont[4] = cont[4] + 1

print(max(cont))
print(cont)

