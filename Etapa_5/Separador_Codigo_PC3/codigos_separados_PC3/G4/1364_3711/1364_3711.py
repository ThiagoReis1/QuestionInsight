from math import *
vi = float(input("velocidade inicial"))
d = float(input("distancia"))
alfa = (asin(d*(9.8/vi**2))*90/pi)
print(round(alfa,2))