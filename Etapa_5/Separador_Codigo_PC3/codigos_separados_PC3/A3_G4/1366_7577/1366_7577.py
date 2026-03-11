import math
pi = math.pi

angulo = float(input("angulo: "))
vel = float(input("velocidade: "))
g = 9.8
sin = math.sin
d = vel**2*(sin(2*math.radians(angulo))/g)
print(round(d,2))