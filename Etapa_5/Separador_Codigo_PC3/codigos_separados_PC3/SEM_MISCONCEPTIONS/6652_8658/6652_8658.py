from numpy import *

notas = array(eval(input()))
peso = [2, 2, 6, 1]
np = sum(notas*peso)/sum(peso)
print(round(np, 2))