from numpy import *
notas = array(eval(input()))
pesos = [1,2,3]
print(round(sum(notas * pesos)/sum(pesos), 2))