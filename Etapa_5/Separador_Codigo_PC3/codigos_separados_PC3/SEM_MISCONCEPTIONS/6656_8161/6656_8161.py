from numpy import *
pesos = [3,4,2,1,4,5]
notas = array(eval(input()))

n = pesos * notas
x = sum(n)
m = x/sum(pesos)

print(round(m, 2))
