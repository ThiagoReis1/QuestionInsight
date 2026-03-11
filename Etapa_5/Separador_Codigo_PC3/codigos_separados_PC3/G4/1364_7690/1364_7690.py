from math import*
vi= float(input("velocidade inicial: "))
d = float(input("distancia: "))
g = 9.8
a = asin(d*(g/vi**2))*(90/pi)
print(round(a,2))