from math import*

angulo = float(input("Angulo da flexa ao sair do arco: "))
d = float(input("Distancia entre voce e a criatura FALMER, em metros: "))

a = radians(angulo)

g = 9.8

v0 = sqrt( d * (g / (sin( 2*a )) ) )

print(round(v0, 2))