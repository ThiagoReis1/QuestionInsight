from math import *

# faça seu código aqui!
lado = float(input())

ap = lado /  (2 * tan(pi/6))
area = 3 * lado * ap

print(round(area, 2))