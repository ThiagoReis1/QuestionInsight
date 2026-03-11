from math import *
v0 = float(input("Qual a velocidade inicial em m/s? "))
d = float(input("Qual a distancia entre em m? "))
g = input("9.8 m/s ** 2: ")) 
angulo = asin(d * g / v0 ** 2) * 90 / pi
print(round(angulo, 2))

