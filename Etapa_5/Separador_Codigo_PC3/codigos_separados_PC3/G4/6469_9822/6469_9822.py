from math import *

# faça seu código aqui!

lado = float(input())

k = 2*tan(pi/6)
apotema = lado/k
area = 3 * lado * apotema

print(round(area,2))