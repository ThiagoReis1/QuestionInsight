from math import *

lado = float(input(" "))

apotema = lado / ( 2 * tan(pi / 11))
areaundecagono = 11 * lado * apotema / 2


print(round(areaundecagono, 2))