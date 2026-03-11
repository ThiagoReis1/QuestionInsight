from math import*
a=radians(float(input("Angulo: ")))
d=float(input("Distancia "))
g=9.8
vo= sqrt(d*(9.8/(sin(2*a))))
print(round(vo,2))