from numpy import *
vetor = array(eval(input()))


soma=0
for i in range(len(vetor)):
    if(vetor[i] > 80):
        soma=soma+vetor[i]-vetor[i]*0.15
    else:
        soma=soma+vetor[i]

print(round(soma,2))
 




 