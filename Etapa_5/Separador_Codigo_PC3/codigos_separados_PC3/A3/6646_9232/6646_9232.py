from numpy import *

notas = array(eval(input('notas: ')))
i = 0
peso = [1, 2, 3]

final1 = notas[0] * 1
final2 = notas[1] * 2
final3 = notas[2] * 3

media = round(((final1 + final2 + final3)/6), 2)

print(media)
