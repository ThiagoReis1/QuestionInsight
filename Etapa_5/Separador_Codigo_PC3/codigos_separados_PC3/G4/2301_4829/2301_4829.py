from math import *
b = float(input("lado b:"))
c = float(input("lado c:"))
angulo = float(input("angulo:"))
a = radians(angulo)
form = ((b**2)+(c**2)-2*b*c*cos(a))**0.5

print(round(form, 2))