from numpy import *

notas = array(eval(input("Quais sao as notas?: nota(1), nota(2), nota(3), nota(4), nota(5), nota(6): ")))
pesos = array([3, 4, 2, 1, 4, 5])

total = sum(pesos * notas) / sum(pesos)

print(round(total,2))


