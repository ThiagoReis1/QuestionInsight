from math import *

# faça seu código aqui!

comprimento_lado = float(input())
apotema = comprimento_lado / (2 * tan(pi / 9))
area_eneagono_arredondada = (9 * comprimento_lado * apotema) / 2

print(round(area_eneagono_arredondada, 2))