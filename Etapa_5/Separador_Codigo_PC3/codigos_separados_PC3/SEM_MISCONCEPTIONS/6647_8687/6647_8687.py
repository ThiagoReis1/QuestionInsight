from numpy import *

notas = array(eval(input("Notas: ")))

nota1 = notas[0] * 2
nota2 = notas[1] * 1
nota3 = notas[-1] * 5

total_notas = (nota1 + nota2 + nota3) / 8

print(round(total_notas, 2))