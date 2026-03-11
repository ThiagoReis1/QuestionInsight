from math import *
lado = float(input("Digite o valor do lado: "))
apotema = lado/(2*tan(pi/6))
area = 3*lado*apotema
print(round(area,2))
