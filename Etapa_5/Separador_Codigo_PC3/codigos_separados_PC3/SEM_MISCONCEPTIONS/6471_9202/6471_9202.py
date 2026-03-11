from math import *
l = int(input("lado"))
apotema = l/(2*tan(pi/8))
area = apotema*4*l
print(round(area,2))
