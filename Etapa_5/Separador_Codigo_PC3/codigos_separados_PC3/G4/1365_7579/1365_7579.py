from math import *

##

a = radians(float(input('digite o angulo:')))
d = float(input('digite a distancia:'))

g = 9.8

v = sqrt(d * (g / sin(2 * a)))

print(round(v,2))
