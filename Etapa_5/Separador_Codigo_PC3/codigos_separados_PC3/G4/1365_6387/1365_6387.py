from math import * 
a = radians(float(input("Angulo da flehca: ")))
b = float(input("Distancia sua e da arvore: "))
g = 9.8

v = sqrt(b * (g/(sin(2*a))))
print(round(v,2))