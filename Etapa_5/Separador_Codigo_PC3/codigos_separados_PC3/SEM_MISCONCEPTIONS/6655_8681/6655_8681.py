from numpy import *

nota = array(eval(input("Conjunto de notas: ")))
peso = array([5,1])

media = ((nota[0]*peso[0]) + (nota[-1]*peso[-1])) / sum(peso)

print(round(media,2))