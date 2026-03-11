from math import*

b = float(input(": "))
c = float(input(": "))
ang = radians (float(input(": ")))

a = sqrt(b ** 2 + c ** 2 - 2 * b * c * cos(ang))

print(round(a, 2))
