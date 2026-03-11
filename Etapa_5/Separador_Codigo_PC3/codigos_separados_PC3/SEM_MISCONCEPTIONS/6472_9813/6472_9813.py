from math import *

# faça seu código aqui!
lados = float(input("O valor dos lados: "))

apotema = lados / (2 * tan(pi/9))
area = 9 * lados * apotema / 2

print(round(area, 2))