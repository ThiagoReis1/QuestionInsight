from math import *

x=float(input("comprimento do lado do octagono:"))

apotema=x/(2*tan(pi/8))
area=4*x*apotema

print(round(area,2))