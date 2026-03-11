from math import tan, pi

lados = int(input(""))

apotema = lados / (2 * tan(pi/5))
area = (5 * lados * apotema) / 2

print("{:.2f}".format(area))