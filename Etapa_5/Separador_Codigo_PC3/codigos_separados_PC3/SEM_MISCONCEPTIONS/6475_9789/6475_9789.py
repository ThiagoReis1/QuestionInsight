from math import*

lado = float(input("lado da fg:"))

opotema = lado / (2 * tan(pi/12))

area = (6 * lado * opotema)

print(round(area, 2))


