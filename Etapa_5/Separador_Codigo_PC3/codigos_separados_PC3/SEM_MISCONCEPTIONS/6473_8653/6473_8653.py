from math import *

# faça seu código aqui!
lado = float(input())
apotema = lado / (2 * tan(pi / 10))
AreaDecagono = 5 * lado * apotema
print(round(AreaDecagono, 2))