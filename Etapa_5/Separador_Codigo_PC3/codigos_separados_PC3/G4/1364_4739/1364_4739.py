v= float(input("velocidade inicial: "))
d= float(input("distancia do alvo: "))
import math
g=9.8
a= math.asin((d*g)/(v**2))*90/math.pi
print(round(a, 2))