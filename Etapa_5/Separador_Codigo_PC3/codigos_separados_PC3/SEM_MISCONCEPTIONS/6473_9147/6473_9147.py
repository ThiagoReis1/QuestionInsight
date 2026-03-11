from math import *

# faça seu código aqui!

comprimento_lado_decagono = float(input("Digite o comprimento do lado do decagono: "))

apotema = comprimento_lado_decagono / (2 * tan(pi / 10))

area_decagono = 5 * comprimento_lado_decagono * apotema

print(round(area_decagono, 2))