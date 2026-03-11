from math import*

A = float(input("Ângulo da flecha:"))
D = float(input("Distância entre você e um determinado Falmer:"))

g = 9.8
VI = sqrt(D*g / sin(2*radians(A)))

print(round(VI,2))