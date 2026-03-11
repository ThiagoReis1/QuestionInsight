from math import*

lado_b = float(input("digite o valor:"))
lado_c = float(input("digite o valor:"))
y = radians(float(input("digite um valo:")))

a = sqrt(lado_b**2 + lado_c**2 - 2*lado_b * lado_c * cos(y))
print(round(a, 2))