from math import *

# entrada do comprimento do decagono
lado = float(input("determine o comprimento do decagono"))

# formula da apotema
apotema = lado/(2*tan(pi/12))

area = 6 * lado * apotema

print(round(area, 2))