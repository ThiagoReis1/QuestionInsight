from math import *
a = float(input("angulo da flecha"))
d = int(float(input("distancia sua e da arvore")))
g = 9.8

b = asin(d*(g/(a**2)))*(90/pi)
print(round(b,2))
