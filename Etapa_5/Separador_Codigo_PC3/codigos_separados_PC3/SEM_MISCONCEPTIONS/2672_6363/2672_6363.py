from math import*

r = float(input("Raio do poligono: "))
lados = int(input("Numero de lados: "))
area = 0.5 * ((r * cos(pi/lados))**2 * tan(pi/lados))
print(round(area, 2))