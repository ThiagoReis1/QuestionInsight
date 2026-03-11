from math import*
a = float(input("angulo da flecha:"))
d = float(input("distancia:"))
g=9.8
sen = radians(a)
Vo = sqrt(d*(g/sin(2*sen)))

print(round(Vo, 2))