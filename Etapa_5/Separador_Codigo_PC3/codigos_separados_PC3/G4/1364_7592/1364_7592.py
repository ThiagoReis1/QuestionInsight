from math import asin, pi

a = float(input("velocidade inicial"))
d = float(input("distancia"))
g = 9.8

x = asin( d * (g/(a**2))) * (90/pi)

print(round(x, 2))









