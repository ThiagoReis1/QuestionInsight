from math import *

lado = float(input())
x = pi/8
apotema = lado/ (2* tan (x))

y =  (lado) * (apotema)

area_p = 4 * y


result= round(area_p, 2)
print(result)