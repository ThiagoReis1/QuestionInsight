from numpy import *

notas = array(eval(input("Digite o vetor de notas: ")))

pesos = array([3,2,4,1,3])

mp = sum(notas*pesos) / sum(pesos)

print(round(mp,2))