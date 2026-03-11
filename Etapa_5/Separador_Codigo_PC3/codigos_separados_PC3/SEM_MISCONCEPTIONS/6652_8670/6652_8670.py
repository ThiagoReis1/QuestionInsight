from numpy import *

nota = array(eval(input("Informe as notas: ")))

peso = array([2,2,6,1])

media = (sum(peso * nota)) / sum(peso)

print(round(media, 2))

