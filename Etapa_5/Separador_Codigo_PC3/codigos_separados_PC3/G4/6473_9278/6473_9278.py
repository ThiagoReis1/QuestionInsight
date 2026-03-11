from math import *

cld = int(input(" Comprimento do lado do decagono: "))

apt = (cld) / (2 * tan(pi/10))

ad = (5 * cld * apt)

print(round(ad,2))