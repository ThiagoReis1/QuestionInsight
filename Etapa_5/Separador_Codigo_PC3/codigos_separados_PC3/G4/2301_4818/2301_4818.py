from math import*

lb=float(input("lado b:"))
lc=float(input("lado c:"))
angulo=float(input("angulo entre b e c:"))

a= sqrt((lb**2+lc**2)-2*(lb*lc)*cos(radians(angulo)))

print(round(a, 2))