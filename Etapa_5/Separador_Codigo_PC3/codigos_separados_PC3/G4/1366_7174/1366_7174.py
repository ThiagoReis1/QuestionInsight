from math import *
ang=radians(float(input(" ")))
vi=float(input(""))
g=9.8
d=(vi**2)*((sin(2*ang))/g)

print(round(d, 2))