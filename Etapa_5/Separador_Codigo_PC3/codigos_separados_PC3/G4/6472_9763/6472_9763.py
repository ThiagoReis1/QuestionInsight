from math import *
lado = float(input("informe o valor do lado: "))

ap = lado / (2*tan(pi/9))
area = (9*lado*ap) / 2

print(round(area, 2))
