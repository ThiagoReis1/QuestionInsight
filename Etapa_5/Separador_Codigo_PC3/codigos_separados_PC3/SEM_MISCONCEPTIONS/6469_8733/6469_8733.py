from math import *

lado= float(input("digite o valor lado do hexagono: "))

apotema =       float(lado /( 2 * tan(pi/6)))
area =        float( 3 * lado * apotema)

print(round(area,2))