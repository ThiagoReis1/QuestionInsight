from math import*
lado = 12
tan = float(input("digite: "))
apotema = lado / (2 * tan ** (pi/12))
area = float (6 * (lado * apotema))
print(round(area, 2))