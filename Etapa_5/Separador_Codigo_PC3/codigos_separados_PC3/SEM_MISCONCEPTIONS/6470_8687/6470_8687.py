from math import *

# faça seu código aqui!
lado = float(input("Digite o lado do heptagono: "))

opotema = lado / (2 * tan(pi/7))

areaHeptagono = (7 * lado * opotema) / 2 

print(round(areaHeptagono, 2))