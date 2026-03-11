from math import *
v=float(input("Digite a velocidade inicial(Vo): "))
d=float(input("Digite a distancia(d): " ))
g=float(9.8)
a=(asin(d*g/v**2)*90/pi)
print(round(a , 2))