# Dados do problema:
b = float(input(""))
c = float(input(""))

from math import*

alpha = radians(float(input("")))

a = sqrt((b)**2 + (c)**2 - 2*b*c*cos(alpha))

print(round(a, 2))



