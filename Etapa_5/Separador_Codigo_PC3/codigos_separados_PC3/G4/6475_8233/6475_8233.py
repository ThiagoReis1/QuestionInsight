from math import *
l = int(input("lado:"))
a = l/(2*tan(pi/12))
area = 6 * l * a
print(round(area, 2))