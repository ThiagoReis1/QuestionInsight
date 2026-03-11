from math import*

a = radians(float(input("angulo: ")))
d = float(input("distancia: "))
g = 9.8



v = (d * g / sin(2 * a)) ** (1/2)




print(round(v, 2))
