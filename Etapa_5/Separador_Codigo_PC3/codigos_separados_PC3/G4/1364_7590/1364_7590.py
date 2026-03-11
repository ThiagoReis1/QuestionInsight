from math import *

vo = float(input("velocidade inicial: "))
d = float(input("distancia: "))

alfa = asin(d*9.8/vo**2)*90/pi

print(round(alfa, 2))

