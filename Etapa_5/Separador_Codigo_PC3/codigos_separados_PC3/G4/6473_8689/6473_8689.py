from math import *

#calculo da area do decagono

l = int(input("informe o valor do lado:")) 
ap = l / (2 * tan(pi / 10))
ad = 5 * l * ap

print (round(ad, 2))