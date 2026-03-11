from math import *
lado = float(input())
x = pi/6
apotema = lado/ (2* tan (x))

y = (lado) * (apotema)
area_p = 6 * y/2

result = round(area_p, 2)
print(result)

