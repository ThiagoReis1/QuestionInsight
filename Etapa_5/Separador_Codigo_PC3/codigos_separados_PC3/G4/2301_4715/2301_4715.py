from math import*
b = float(input("lado b: "))
c = float(input("lado c: "))
ang = radians(float(input("o angulos entre eles: ")))
a = sqrt((b ** 2) + (c ** 2) - 2 * b * c * cos(ang))
print(round(a, 2))