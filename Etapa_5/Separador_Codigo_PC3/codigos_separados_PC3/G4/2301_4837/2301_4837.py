from math import*

b = float(input("lado b: "))
c = float(input("lado c: "))
d = float(input("angulo alfa entre b e c: "))

a = sqrt((b**2)+(c**2)-(2*bc*cos(d)))

print(round(a, 2))