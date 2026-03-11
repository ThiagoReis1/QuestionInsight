from math import *

b = float(input("Digite o valor do lado b: "))
c = float(input("Digite o valor do lado c: "))
angulo = radians(float(input("Digite o valor do angulo entre b e c: ")))

A = sqrt((b**2)+(c**2)-(2*b*c*cos(angulo)))

print(round(A, 2))