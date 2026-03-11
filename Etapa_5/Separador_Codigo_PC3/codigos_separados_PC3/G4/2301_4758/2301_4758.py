from math import *
lb = float(input("Valor do lado b: "))
lc = float(input("Valor do lado c: "))
an = float(input("Valor do angulo entre b e c: "))
ang = radians(an)
a = ((lb**2)+(lc**2)-2*lb*lc*cos(ang))**0.5

print (round(a,2))