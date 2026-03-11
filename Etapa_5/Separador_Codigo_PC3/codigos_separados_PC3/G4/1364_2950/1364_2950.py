from math import *

v0 = float(input())
d = float(input())

a = asin((d*9.8)/(v0**2))*(90/pi)

print(round(a,2))