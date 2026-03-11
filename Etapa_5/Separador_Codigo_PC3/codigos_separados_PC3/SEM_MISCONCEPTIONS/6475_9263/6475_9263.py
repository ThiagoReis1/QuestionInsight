from math import pi
from math import tan

lado = float(input("valor lado: "))

apotema = lado / (2*tan(pi/12))

area = 6 * lado * apotema

print(round(area,2))