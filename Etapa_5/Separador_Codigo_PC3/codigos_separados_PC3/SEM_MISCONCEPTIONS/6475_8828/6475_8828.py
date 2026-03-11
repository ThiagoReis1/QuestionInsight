from math import *

lado = float(input("lado: "))
apotema = lado/(2*tan(pi/12))
area= 6*lado*apotema
print(round(area,2))