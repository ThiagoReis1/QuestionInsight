from math import *

# faça seu código aqui!
lado = int(input("digite a quantidade de lados:"))
apotema = lado/(2 * tan(pi/8))
areaoctogo = 4 * lado * apotema
print(round(areaoctogo,2))