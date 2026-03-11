from math import*
v0 = float(input("velocidade inicial: "))
d = float(input("distancia: "))
g = 9.8
a = asin(d*(g/v0**2))*(90/pi)
print(round(a, 2))