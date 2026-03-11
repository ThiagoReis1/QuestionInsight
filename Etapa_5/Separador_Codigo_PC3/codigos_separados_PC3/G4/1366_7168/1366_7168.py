from math import *
a = float(input("Qual o angulo que a flecha saiu: "))
v = float(input("Qual a velocidade que a flecha saiu: "))
g = float(9.8)
d = (v ** 2) * (sin(radians(a * 2)) / g);
print(round(d, 2))