from math import  *

a = float(input("comprimento"))

v = a / (2*tan (pi/11))
r = (11*a*v)/2

print(round(r , 2))