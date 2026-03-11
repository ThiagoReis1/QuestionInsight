from math import *

v=float(input())
d=float(input())
g=float(9.8)

a=asin(d*g/v**2)*90/pi

print(round(a,2))