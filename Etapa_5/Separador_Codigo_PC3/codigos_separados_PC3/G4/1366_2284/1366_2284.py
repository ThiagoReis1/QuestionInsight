from math import*

ang = float(input("Ângulo: "))
vi = float(input("Velocidade inicial: "))

d = (sin(2*ang)) * (vi**2) / 9.8

print(round(d, 2))