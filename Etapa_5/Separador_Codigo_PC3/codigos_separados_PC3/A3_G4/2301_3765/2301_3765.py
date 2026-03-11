from math import *

b = float(input("lado b: "))
c = float(input("lado c: "))
bc = float(input("angulo b, c: "))

a = sqrt((b**2)+(c**2)-cos(2*b*c))

print(round(a, 2))