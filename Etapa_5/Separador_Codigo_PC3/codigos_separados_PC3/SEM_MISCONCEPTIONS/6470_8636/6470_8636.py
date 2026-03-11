from math import *
lado = int(input("comprimento do lado: "))

apotema = lado / (2*tan(pi/7))
areaH = 7 * lado * apotema / 2

print(round(areaH, 2))