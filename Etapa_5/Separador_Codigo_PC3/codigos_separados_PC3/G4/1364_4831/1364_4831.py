from math import *
v = float(input("v: "))
d = float(input("d: "))
g = 9.8 
a = asin(d*(g/v**(2))) * 90/pi

print(round(a,2))