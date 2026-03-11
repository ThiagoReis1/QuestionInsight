from math import *

# faça seu código aqui!

l = float(input("Informe o valor do lado do heptagono: "))

apo = l / (2 * (tan(pi/7)))

area = (7 * l * apo) / 2

print(round(area, 2))