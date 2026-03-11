from math import *
l = float(input("lado: "))
apotema = l/(2*tan(pi/6))
area = 3*l*apotema
print(round(area, 2))