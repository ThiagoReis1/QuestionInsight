from math import*

b = float(input("lado b: "))
c = float(input("lado c: "))
ang = radians(float(input("angulo: ")))

a = sqrt(b**2 + c**2 - 2*b*c*cos(ang))

print(round(a, 2))
