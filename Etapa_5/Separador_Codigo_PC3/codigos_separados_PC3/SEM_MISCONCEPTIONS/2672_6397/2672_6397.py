from math import *
raio = float(input("valor do raio: "))
latos =  float(input("numero de lados: "))

area = 0.5 * (( raio * cos (pi/latos))**2 * tan (pi/latos))

print(round(area,2))