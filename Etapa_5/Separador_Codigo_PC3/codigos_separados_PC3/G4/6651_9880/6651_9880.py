from numpy import *

nota = array(eval(input("Insira o conjunto de notas: ")))

peso = [5, 4, 3, 2]

v = nota * peso

media = sum(v) / sum(peso)

print(round(media, 2))
