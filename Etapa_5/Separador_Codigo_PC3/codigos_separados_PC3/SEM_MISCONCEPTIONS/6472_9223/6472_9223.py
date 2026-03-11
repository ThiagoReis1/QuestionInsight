from math import *
c = float(input("o comprimento do poligono:"))
apotema = c/(2*tan(pi/9))
areaPoligono = 3*c*apotema
v = apotema+areaPoligono - c

print(round(v,2))