from numpy import *

notas = array(eval(input()))
pesos = array([5, 1])

mp = sum(notas * pesos) / sum(pesos)

print(round(mp, 2))