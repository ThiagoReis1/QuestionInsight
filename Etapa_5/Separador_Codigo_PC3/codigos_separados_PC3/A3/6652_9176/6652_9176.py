from numpy import *
pesos = [2,2,6,1]
notas = array(eval(input("Digite as respectivas notas: ")))
i = 0
j = 0
tam = size(pesos)
while i < size(pesos):
 notas[j] = notas[j] * pesos[i]
 j += 1
 i += 1
media = (sum(notas)/sum(pesos))
print(round(media, 2))