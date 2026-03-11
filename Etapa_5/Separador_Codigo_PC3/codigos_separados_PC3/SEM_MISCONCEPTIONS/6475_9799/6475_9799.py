from math import *

lado = float(input())

apotema = lado/(2*tan(pi/12))

area_P = (6 * lado*apotema)

print(round(area_P, 2))