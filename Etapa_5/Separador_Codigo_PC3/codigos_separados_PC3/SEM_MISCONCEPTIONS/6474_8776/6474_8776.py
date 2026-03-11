from math import *

# faça seu código aqui!

lado = int(input("Lados do undecagono: "))

apotema = lado/(2*tan(pi/11))

area = (11 * lado * apotema)/2
print(float(round(area, 2)))
