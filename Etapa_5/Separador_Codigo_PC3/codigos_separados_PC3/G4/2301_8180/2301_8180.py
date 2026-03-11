from math import*
b = float(input("o lado b: "))
c = float(input("o lado c: "))
var = float(input("valor entre b e c: "))
var1 = float(radians(var))
a = sqrt((b ** 2) + (c ** 2) - (2 * b * c * (cos(var1))))
print(round(a, 2))