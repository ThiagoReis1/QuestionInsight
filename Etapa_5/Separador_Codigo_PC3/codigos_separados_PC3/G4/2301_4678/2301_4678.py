from math import radians
from math import cos
from math import sqrt

Lb = float(input("Lado b: "))
Lc = float(input("Lado c: "))
ang = radians(float(input("Angulo: ")))

a = sqrt((Lb**2) + (Lc**2) - (2* Lb * Lc * cos(ang)))

print(round(a, 2))