from math import *

comprimento = int(input())

apotema = comprimento/(2*tan(pi/12))

Area = 6 * comprimento * apotema

print(round(Area, 2))