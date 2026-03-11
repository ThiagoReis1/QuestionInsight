from numpy import *
notas= array(eval(input()))

i = 0
pesos = [2,2,6,1]
m=pesos*notas
soma = sum(m)
media = soma/sum(pesos)

print(round(media, 2))