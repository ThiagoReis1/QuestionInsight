from math import *

var1 = float(input("Digite um comprimento: "))

apotema = var1 / (2* tan(pi / 7))
area = ( 7 * var1 * apotema) / 2
print (round(area,2))