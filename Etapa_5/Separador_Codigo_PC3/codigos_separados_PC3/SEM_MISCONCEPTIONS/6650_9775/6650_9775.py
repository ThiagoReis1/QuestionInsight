from numpy import *
notas = array(eval(input()))
peso = [4,3]

numr = notas * peso
media = sum(numr) / sum(peso)
print(round(media, 2))