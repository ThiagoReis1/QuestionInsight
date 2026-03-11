from math import pi, asin
v = float(input("velocidade inicial"))
d = float(input("distancia"))
g = 9.8
x = asin((d) * (g) / (v**2)) * 90 / pi
print(round(x, 2))