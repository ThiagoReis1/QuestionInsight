from numpy import *
notas= array(eval(input(" ")))
peso = array([1,2,3])
num = notas * peso
media = sum(num) / sum(peso)
print(round(media, 2))