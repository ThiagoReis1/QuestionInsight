from math import*
a = radians(float(input("Digite o angulo da flecha:")))
d = float(input("Digite a distancia entre voce e Falmer:"))
g = 9.8
v0 = sqrt(d * (g / sin(2 * a)))

print(round(v0, 2))