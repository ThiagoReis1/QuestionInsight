# Lados do triangulo
b = float(input("Lado b: "))
c = float(input("Lado c: "))

from math import*

# angulo entre b e c
d = radians(float(input("Angulo entre b e c: ")))

var = (b**2) + (c**2) - 2*b*c*(cos(d)) 

a =(var)**0.5

print(round(a, 2))


