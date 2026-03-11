from math import *
r = float(input("insira o valor do raio do poligono: "))
n = int(input("insira a quantidade de lados do poligono: "))
c = r*cos(pi/n)
print(round(c, 2))