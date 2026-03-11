from math import *

# faça seu código aqui!
lado= float(input("Insira o valor do lado: "))
apotema= lado / (2 * tan(pi / 6))

area_hexagono= 3 * lado * apotema 

print(round(area_hexagono, 2))