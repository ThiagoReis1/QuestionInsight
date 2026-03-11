from math import*

a =  radians(float(input("Angulo: ")))
d =  float(input("Distancia: "))
g = 9.8


v0 = sqrt(d*(g/sin(2*a)))
print(round(v0, 2))