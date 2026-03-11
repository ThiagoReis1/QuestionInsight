from math import *
r = float(input("raio"))
n = int(input("lados"))
area = 1/2 * ((r * cos(pi/n))**2 * tan(pi/n))
print(round(area, 2))