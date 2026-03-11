from math import *

b = float(input("lado b: "))
c = float(input("lado c: "))
x = float(input("b e c em graus: "))

a = sqrt((b**2 + c**2)-2*b*c*cos(radians(x)))

print(round(a, 2))