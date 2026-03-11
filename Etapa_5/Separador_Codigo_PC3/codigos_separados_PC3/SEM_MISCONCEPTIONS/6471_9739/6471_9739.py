from math import *

# faça seu código aqui!

lado = float(input("Informe o comprimento do lado: "))
apotema = lado/(2*tan(pi/8))
area_octogono = 4 * lado * apotema

print(round(area_octogono, 2))