from math import *

a = int(input("comprimento do lado do octogono: "))

ap = a/(2*tan(pi/8))

area_oct = 4 * a * ap

print(round(area_oct,2))