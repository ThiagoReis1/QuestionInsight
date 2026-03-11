from math import *

v = float(input("velocidade:"))
d = float(input("distancia: "))

grau = asin((d*9.8/(v)**2))*90/pi

print(round(grau,2))