
from math import *

a = radians(float(input("angulo ")))
d = float(input("distancia "))
g = 9.8

vi = sqrt(d * (g / sin(2 * a)))

print(round(vi, 2))




