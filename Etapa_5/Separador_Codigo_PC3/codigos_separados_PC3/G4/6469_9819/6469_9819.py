from math import *

# faça seu código aqui!
lado = float(input("Insira o comprimento do lado do hexagono "))
aptm = lado / (2 * tan(pi/6))
area = 3 * lado * aptm
print(round(area,2))