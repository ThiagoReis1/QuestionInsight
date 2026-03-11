from math import *
v = float(input("digite o valor da velocidade: "))
d = float(input("digite o valor da distancia: "))
x = (asin(d*9.8/v**2) * (90/pi))

print(round(x, 2))

