from math import*
b = float(input("lado b :"))
c = float(input("lado c :"))
a = float(input("angulo a :"))
a = sqrt(b**2+c**2-2*b*c*cos(radians(a)))
print(round(a ,2))