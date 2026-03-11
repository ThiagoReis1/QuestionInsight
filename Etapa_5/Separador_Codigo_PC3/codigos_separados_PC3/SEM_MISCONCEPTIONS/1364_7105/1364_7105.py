from math import *

velocidade = float(input())
distancia = float((input()))
eq = asin((distancia*9.8)/(velocidade*velocidade))
babado = eq* (90/pi)




print(round(babado,2))