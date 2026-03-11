from math import*
a = radians(float(input("angulo da flecha: ")))
vi = float(input("velocidade inicial: "))
d = ((vi**2)*(sin(2*a)/9.8))
print(round(d,2))