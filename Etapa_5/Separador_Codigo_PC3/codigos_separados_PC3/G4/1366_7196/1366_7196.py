from math import*

ang = radians(float(input("Angulo da flecha: ")))
vi = float(input("Velocidade inicial: "))

g = 9.8

d = vi**2 * sin(2*ang)/g

print(round(d,2))