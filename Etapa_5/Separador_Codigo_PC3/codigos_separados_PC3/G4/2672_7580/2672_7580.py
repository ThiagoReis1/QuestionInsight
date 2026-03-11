from math import *
raio = float(input('raio do poligono: '))
n = int(input('numero de lados: '))
area = 0.5 * ( ((raio*cos(pi/n))**2)*tan(pi/n) )
print(round(area,2))