from math import *


a = float(input("Digite o lado b:"))
b = float(input("Digite o lado c:"))
g = radians(float(input("Digite o angulo entre b e c (em graus)")))

c = sqrt(a**2 + b**2 - 2*a*b*cos(g))

print(round(c, 2))