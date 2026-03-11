from math import*

a = radians(int(input("Angulo da flecha : ")))
d = float(input("distancia : "))
g = 9.8

v0 = sqrt((d * g) / (sin(2 * a)))

print(round(v0, 2))