from math import *

lado_eneagono = int(input())

apotema = lado_eneagono / (2*tan(pi/9))
area_eneagono = (9*lado_eneagono*apotema) / 2

print(round(area_eneagono,2))