from math import *

# faça seu código aqui!
lado = int(input("Diga o lado: "))


apotema =  lado / (2 * tan (pi / 8))

area = 4 * lado * apotema



print(round(area,2))
