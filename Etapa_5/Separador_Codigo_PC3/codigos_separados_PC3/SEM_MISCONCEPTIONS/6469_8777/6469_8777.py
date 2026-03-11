from math import *
lado =  float(input("comprimento:"))
apoterna = lado / (2 * tan(pi/6))
areaHexagono = 3*lado*apoterna


print(round(areaHexagono, 2))