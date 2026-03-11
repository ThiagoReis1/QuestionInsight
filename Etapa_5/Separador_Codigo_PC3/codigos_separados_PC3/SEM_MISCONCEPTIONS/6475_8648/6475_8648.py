#Varivavel de Entrada
lado = float(input("Digite o valor: "))
#Calculo Opotema
from math import *
opotema = lado / (2 * tan(pi/12))
#Calculo Área Dodecagono
Area = 6 * lado * opotema
#Resultao
print(round(Area, 2))