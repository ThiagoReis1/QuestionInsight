from math import*
raio = float(input("raio do poligono: "))
n = int(input("numero de lados: "))
l = 2 * raio * sin( pi / n )
print(float(round(l, 2)))