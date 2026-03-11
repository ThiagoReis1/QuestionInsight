from math import *
ang = radians(float(input()))
dist = float(input())
vo = sqrt(dist*((9.8)/sin(2*ang)))
print(round(vo,2))