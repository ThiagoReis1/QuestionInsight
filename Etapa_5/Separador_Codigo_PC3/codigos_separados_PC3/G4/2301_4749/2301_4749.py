from math import *
b = float(input("Digite o lado b: "))
c = float(input("Digite o lado c: "))
a = radians(float(input("Digite o angulo a: ")))
x = sqrt((b**2) + (c**2) - 2 * b * c * cos(a))
print(round(x, 2))