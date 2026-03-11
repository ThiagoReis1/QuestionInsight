from numpy import *
notas = array(eval(input()))
i = 0
peso = [3,4,2,1,4,5]
np = sum(notas*peso)/sum(peso)
print(round(np, 2))