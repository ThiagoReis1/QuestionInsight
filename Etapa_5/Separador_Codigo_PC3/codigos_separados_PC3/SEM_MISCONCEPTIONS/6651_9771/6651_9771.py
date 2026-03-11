from numpy import *

notas = array(eval(input('insira 4 notas: ')))
pesos = array([5, 4, 3, 2])

numero = notas * pesos
media = sum(numero) / sum(pesos)
print(round(media, 2))