from math import *

# faça seu código aqui!
lado = float(input("Quantidade de lados: "))
apotema = (lado) / (2 * tan(pi / 6))
areaHexagono = 3 * lado * apotema
print(round(areaHexagono, 2))