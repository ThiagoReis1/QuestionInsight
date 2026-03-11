from math import *
comprlado = float(input("Comprimento do eneagono: "))

apotene = comprlado / (2 * tan(pi/9))
# faça seu código aqui!

areaene = 9 * comprlado * apotene / 2

print(round(areaene,2))