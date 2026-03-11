from math import *
v = float(input("entre com a velocidade: "))
d = float(input("entre com a distancia: "))
g = 9.8
x = (d*g) / v**2
A = (asin(x)*90 / pi)

print(round(A,2))