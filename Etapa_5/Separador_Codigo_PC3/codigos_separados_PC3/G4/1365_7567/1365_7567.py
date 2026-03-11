from math import*
a = radians(float(input("Angulo da flecha ao sair do arco: ")))
d = float(input("Distancia entre voce e a criatura: "))
g = 9.8
den = sin(2*a)
var = d * (g/den)
vo = sqrt(var)
print(round(vo, 2))