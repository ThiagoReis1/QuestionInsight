from math import *

lado= int(input('o comprimento do lado do eneagono?'))
apotema= lado/ (2 * tan (pi/9))
area= (9 * lado * apotema)/2
print( round (area, 2))