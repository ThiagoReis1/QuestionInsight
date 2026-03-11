from math import *

# faça seu código aqui!
lado_hep = int(input("Comprimento da area do heptagono: "))

apotema = (lado_hep) / (2* tan (pi/7))

areaH = (7 * lado_hep * apotema) / 2

print(float(round(areaH, 2)))