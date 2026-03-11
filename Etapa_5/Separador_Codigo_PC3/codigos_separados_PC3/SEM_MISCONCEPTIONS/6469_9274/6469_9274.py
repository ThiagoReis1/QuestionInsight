from math import *

# faça seu código aqui!

lado_hexag = float(input("Qual o tamanho do lado do hexagono?"))

apotema = lado_hexag / (2 * tan(pi/6))

area_hexag = 3 * lado_hexag * apotema

print(round(area_hexag,2))