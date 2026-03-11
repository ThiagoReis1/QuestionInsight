from math import*

an = float(input("saida da flecha"))
d = float(input("distancia entre dois corpos"))

g=9.8
total = (d * g / sin(radians(2 * an)))**0.5
print(round(total,2))