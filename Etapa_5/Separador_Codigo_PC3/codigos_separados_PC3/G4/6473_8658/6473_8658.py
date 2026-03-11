from math import *

lado = float(input("valor do lado: "))
apo = lado / (2 * tan(pi/10))
area = 5 * lado * apo
print(round(area, 2))