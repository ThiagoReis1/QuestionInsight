# Estimativa de maçãs por metro quadrado:
m = float(input("Qual a estimativa de macas? "))

# Comprimento da aresta:
a = float(input("Qual o comprimento da aresta? "))

from math import *

# area de um hexagono regular:
area_hexagono = 3 * sqrt(3 * a ** 2) / 2

# Quantidade total de maçãs:
print(int(area_hexagono * m))
