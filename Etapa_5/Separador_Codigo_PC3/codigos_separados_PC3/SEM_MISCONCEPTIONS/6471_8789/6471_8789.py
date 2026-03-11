from math import *

lado= float(input())

apotema= lado / (2 * tan (pi/8))

b= 4 * lado * apotema

print(round(b, 2))