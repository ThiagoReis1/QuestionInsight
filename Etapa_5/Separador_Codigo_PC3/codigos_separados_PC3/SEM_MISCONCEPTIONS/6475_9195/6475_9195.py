from math import *

# faça seu código aqui!
l = float(input("comprimento dos lados do pentagono"))

apotema = l / (2* tan(pi/12))
AreaDodecagono = 6*l*apotema
print(round(AreaDodecagono, 2))