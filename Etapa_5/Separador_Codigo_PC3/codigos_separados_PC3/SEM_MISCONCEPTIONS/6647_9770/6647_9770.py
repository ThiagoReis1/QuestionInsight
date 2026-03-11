from numpy import *

notas = array(eval(input()))
pesos = array([2,1,5])

num = notas*pesos
media= sum(num)/sum(pesos)
print(round(media,2))