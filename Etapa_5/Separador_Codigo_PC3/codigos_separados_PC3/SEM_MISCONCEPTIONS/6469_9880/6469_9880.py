from math import *

# Inserindo dados de comprimento do lado do hexagono
l = float(input("Qual o comprimento do lado do hexagono?: "))

# Calculando apotema e area do hexagono
ap = l / (2 * tan(pi / 6))
area_hex = 3 * l * ap

#Imprimindo area do hexagono
print(round(area_hex, 2))