from math import*

VO = float(input("Digite velocidade inicial: "))
d = float(input("Digite a distancia entre voces: "))

g=9.8

d1=(d*(g/VO**2))

a = asin(d1)*(90/pi)

print(round(a,2))