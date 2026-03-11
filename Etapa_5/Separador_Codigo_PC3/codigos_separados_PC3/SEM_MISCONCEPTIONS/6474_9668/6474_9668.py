from math import *

lado= float(input("qual o lado do undecagono?"))

apotema= lado / (2 * tan (pi / 11))

area_unde= (11 * lado *apotema) / 2

print(round( area_unde, 2))