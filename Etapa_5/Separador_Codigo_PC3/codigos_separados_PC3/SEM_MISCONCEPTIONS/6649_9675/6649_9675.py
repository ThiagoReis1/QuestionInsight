from numpy import *

notas = array(eval(input()))

pesos = [3,2,4,1,3]

media_ponderada = sum(notas*pesos)/sum(pesos)

print(round(media_ponderada,2))