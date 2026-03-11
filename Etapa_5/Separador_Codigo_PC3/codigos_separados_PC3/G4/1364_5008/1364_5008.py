import math
v0 = float(input("v0: "))
d = float(input("d: "))
print(round(math.asin((d*9.8)/v0**2)*90/math.pi, 2))