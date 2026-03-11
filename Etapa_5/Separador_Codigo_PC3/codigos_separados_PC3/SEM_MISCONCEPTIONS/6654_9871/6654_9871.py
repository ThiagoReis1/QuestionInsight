from numpy import *

pesos = [1,3,2,5]

notas = eval(input(" "))

notas1 = pesos[0] * notas[0]
notas2 = pesos[1] * notas[1]
notas3 = pesos[2] * notas[2]
notas4 = pesos[3] * notas[3]

media = (notas1 + notas2  + notas3 + notas4) / 11
print(round(media, 2))