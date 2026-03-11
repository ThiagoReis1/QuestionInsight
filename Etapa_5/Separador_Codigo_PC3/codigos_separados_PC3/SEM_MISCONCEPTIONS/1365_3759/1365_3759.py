from math import *
angulo = radians(float(input("Digite aqui o angulo em graus:")))
d = float(input("Digite aqui a distancia em metros:"))
g = 9.8
velocidade_inicial= (sqrt(d * g / sin(2 * angulo)))

print(round(velocidade_inicial,2))