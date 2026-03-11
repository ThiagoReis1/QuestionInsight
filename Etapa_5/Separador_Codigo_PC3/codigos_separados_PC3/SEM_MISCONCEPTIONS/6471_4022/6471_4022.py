from math import pi
from math import tan

lado = float(input("comprimento do lado do octagono: "))

apotema = lado / (2 * tan(pi/8))
areaoc = 4 * lado * apotema

print(round(areaoc, 2))