from numpy import *

notas = array(eval(input("Escreva as notas: ")))

n1 = notas[0]*5
n2 = notas[1]*4
n3 = notas[2]*3
n4 = notas[3]*2

med = (n1 + n2 + n3 + n4) / 14

print(round(med, 2))