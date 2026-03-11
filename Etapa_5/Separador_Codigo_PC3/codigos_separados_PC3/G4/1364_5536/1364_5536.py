from math import *
v1 = float(input(" velocidade inicial "))
d = float(input(" ditancia "))
a = asin(d * 9.8/v1 ** 2) * 90/pi
print(round(a, 2))