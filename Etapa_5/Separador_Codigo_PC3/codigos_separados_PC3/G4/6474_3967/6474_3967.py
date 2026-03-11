from math import *

lado = float(input())

apot = lado / (2 * tan(pi/11))

area = 11 * lado * apot / 2

print(round(area,2))