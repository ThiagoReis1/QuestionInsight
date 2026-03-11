from math import *

lado= (float(input("comprimento do lado do octogono: ")))


Apotema = lado / (2 * tan(pi/8))

Ao = 4 * lado * Apotema 

print(round(Ao,2))