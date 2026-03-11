from math import *
v = float(input("Velocidade(m/s):"))
d = float(input("Distancia(m):"))
g = 9.8
a = asin(d*g/v**2)*90/pi
print(round(a,2))
