from numpy import *

notas = eval(input("Digite o vetor de notas: "))
pesos = array([2,1,5])
media_ponderada  = sum (notas * pesos) / sum(pesos)
media_ponderada = round(media_ponderada,2)
print(media_ponderada)