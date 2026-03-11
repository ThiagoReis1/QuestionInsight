from math import *
ang=float(input("entre com o angulo da flecha:  "))
g=9.8
d=float(input("entre com a distancia da fera:  "))
v=(d*(g/sin(radians(2*ang))))**0.5
print(round(v, 2))