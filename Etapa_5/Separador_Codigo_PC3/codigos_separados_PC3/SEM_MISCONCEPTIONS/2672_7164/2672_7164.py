raio = float(input("Raio r do poligono: "))
nlados = int(input("Numero de lados do poligono: "))
from math import*
print(round((0.5*(raio*cos(pi/nlados))**2)*tan(pi/nlados),2))