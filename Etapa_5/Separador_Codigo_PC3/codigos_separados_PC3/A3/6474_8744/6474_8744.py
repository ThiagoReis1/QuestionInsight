from math import tan
from math import pi

# faça seu código aqui!

lados = 11

lado =  float(input("digite o comprimento: "))

apotema = lado / (2 * tan (pi/11))

area = (11 * lado * apotema) / 2

print(round(area,2))