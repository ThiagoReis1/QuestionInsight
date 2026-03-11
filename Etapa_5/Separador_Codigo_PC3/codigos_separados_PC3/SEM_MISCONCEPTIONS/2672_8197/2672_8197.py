from math import *

raio_r = float(input("Qual o raio 'r'? "))
lados_n = int(input("Quantos lados 'n' tem? "))

area = 1/2 * ((raio_r * cos (pi / lados_n))**2 * tan(pi / lados_n))

print(round(area,2))