from math import *

# faça seu código aqui!

lado = float(input("Comprimento do lado: "))

apotema = lado / (2 * tan(pi/10))

Area_Decagono = 5 * lado * apotema
print(round(Area_Decagono, 2))