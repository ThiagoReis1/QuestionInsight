from numpy import *

notas = eval(input("Notas:"))
peso = [5, 4, 3, 2]

n0 = notas[0] * peso[0] 
n1 = notas[1] * peso[1]
n2 = notas[2] * peso[2]
n3 = notas[3] * peso[3]

media = (n0 + n1 + n2 + n3) / 14

print(round(media, 2))