from numpy import * 

vetor = (array(eval(input())))
peso = [1,3,2,5]

v1 = vetor[0]*1
v2 = vetor[1]*3
v3 = vetor[2]*2
v4 = vetor[3]*5

soma = (v1+v2+v3+v4)
soma1 = sum(peso)
media = soma / soma1
print(round(media,2))