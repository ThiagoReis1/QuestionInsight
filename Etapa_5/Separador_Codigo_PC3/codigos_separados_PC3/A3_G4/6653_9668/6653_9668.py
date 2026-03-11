from numpy import *

peso = array([3,5,1])

notas = array(eval(input("notas: ")))

ind = 0

mp = sum(notas * peso) / sum(peso)

print(round(mp,2))