from math import*
b = float(input("lado b: "))
c = float(input("lado c: "))
alfa = float(input("angulo entre b e c: "))
rad = radians (alfa)
a = ((b**2)+(c**2)-2*b*c*cos(rad))**0.5
print (round(a,2))
