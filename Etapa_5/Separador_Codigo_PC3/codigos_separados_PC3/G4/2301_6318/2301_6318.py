from math import *
b= float(input("lado b: "))
c= float(input("lado c: "))
d= float(input("angulo: "))
a= sqrt(b**2+c**2-2*b*c*cos(radians(d)))
print(round(a,2))