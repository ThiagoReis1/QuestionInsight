from math import *

id_heptagono = float(input("Digite o comprimento do lado do heptagono:"))

apotema = id_heptagono/(2 * tan(pi/7))

area = 7*id_heptagono*apotema/2

print(round(area,2))