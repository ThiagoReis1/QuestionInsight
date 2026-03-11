from math import *

lado = float(input("lado da fg:"))

apotema = lado / (2 * tan(pi/8))

area = (4 * lado * apotema)

print(round(area,2))