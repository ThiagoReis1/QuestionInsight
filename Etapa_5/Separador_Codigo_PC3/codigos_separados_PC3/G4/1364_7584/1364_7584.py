#entrada
from math import *

v0 = float(input("Qual a velocidade inicial da flecha ao sair do arco? "))
d = float(input("Qual a distancia de voce e um determinado Falmer? "))

#valor fixo e calculo do angulo
g = 9.8
ang = ((asin(d * (g/(v0 **2)))) * (90/pi))

#saida
print(round(ang, 2))