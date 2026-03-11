from math import *
a = float(input("velocidade inicial:\n"))
b = float(input("distancia:\n"))
g = 9.8
c = 90/pi
e = a*a
d = asin((b*g)/e)
print (round(d*c,2))