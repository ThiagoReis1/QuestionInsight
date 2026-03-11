from math import *

lado = float(input(""))
apotema  = lado / (2 * tan(pi / 8))
AREA = 4 * lado * apotema
print(round(AREA, 2))