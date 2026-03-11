from math import*
a = radians(float(input("angulo em graus: ")))
d = float(input("distancia: "))
g = 9.8
vo = sqrt(d*g/sin(2*a))
#radians(vo)
print(float(round(vo, 2)))

