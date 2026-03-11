from math import *
ang = float(input("valor do angulo "))
d = float(input("valor da distancia "))
g = 9.8
Vo = sqrt((d * g)/sin(radians(2 * ang)))
print(round(Vo,2))