from math import*
a = radians(float(input("angulo desejado:")))
v = float(input("velocidade desejada:"))
g = 9.8
d = (v**2 * (sin(2*a)/g))
print(round(d, 2))

