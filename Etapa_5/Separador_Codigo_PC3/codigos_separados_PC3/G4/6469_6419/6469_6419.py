from math import *

comp = float(input("Digite o comprimento da area do hexagono: "))
ap = comp / (2 * tan (pi / 6))
ah = 3 * comp * ap

print(round(ah, 2))
