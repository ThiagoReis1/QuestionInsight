from math import *

# faça seu código aqui!
lado = float(input("Quanto mede um lado? "))

apotema = lado/(2 * tan(pi / 9))

areaEneagono = (9 * lado * apotema) / 2

print(round(areaEneagono, 2))