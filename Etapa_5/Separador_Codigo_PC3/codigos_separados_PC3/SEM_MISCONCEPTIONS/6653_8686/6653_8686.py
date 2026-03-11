from numpy import *

n = array(eval(input()))
peso = array([3, 5, 1])

media = (n[0] * peso[0] + n[1] * peso[1] + n[2] * peso[2]) / sum(peso)

print(round(media, 2))