from math import *

lado = int(input("Digite o valor do lado:"))

apotema = lado / (2 * tan(pi/5))

pentagono = (5 * lado * apotema) / 2

print(round(pentagono,2))