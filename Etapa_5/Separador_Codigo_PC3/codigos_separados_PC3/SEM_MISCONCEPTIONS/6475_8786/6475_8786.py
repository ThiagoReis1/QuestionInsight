from math import *

lado = int(input("Digite o comprimento do lado do dodecagono: "))

apotema = (lado) / (2 * tan(pi / 12))
areadoca = 6 * lado * apotema

print(round(areadoca, 2))