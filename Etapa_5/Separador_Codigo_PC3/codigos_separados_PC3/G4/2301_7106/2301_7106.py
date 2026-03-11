from math import *
b = float(input("Lado b:  "))
c = float(input("Lado c:  "))
ang = radians(float(input("Angulo entre b e c:  ")))
a = sqrt((b**2)+(c**2)-(2*b*c)*cos(ang))
print(round(a, 2))