from math import*
Vi = float(input("Insira a velocidade incial da flecha ao sair do arco: "))
dist = float(input("Insira a distancia entre voce e um determinado Falmer: "))
g = 9.8
alpha = asin(dist*g/Vi**2) * 90/pi
print(round(alpha, 2))