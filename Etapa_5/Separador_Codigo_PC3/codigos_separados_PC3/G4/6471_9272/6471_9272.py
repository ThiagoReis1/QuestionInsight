from math import *
a = float(input("o comprimento do lado do octogono:"))
x = a / (2 * tan(pi/8))
y = 4 * a * x

print(round(y,2))