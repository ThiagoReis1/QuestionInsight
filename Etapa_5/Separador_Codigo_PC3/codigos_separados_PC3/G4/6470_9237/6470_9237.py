# Area do Heptagono = a
# Apotema = ap
# lado do heptagono = l

from math import *

l = int(input("lado: "))

ap = l/(2 * tan(pi/7))

a = (7 * l * ap)/2


print(round(a, 2))