from math import *

v = float(input(" A velocidade inicial da flecha ao sair do arco, em m/s "))
d = float(input(" A distancia entre voce e um determinado Falmer, em metros "))

g = 9.8

a = asin(d * g/v**2) * (90/pi)

print(round(a, 2))