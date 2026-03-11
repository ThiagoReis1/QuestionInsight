# raio do poligono 
#numeros de lados
from math import *
r = float(input("raio do poligono: "))
l = float(input("numero de lados: "))



a = 1/2 *((r * cos(pi/l))**2 * tan(pi/l))
print(round(a,2))
#area A do triangulo