from math import *

comprimento_lado = float(input("Digite o cm do lado: "))
a1 = comprimento_lado
a2 = 2 * tan(pi/6)
area_hexagono = 3 * comprimento_lado * (a1/a2)

print(round(area_hexagono, 2))