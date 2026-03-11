import math
a = math.radians(float(input("")))
d = float(input(""))
g = 9.8
v0 = math.sqrt(d*(g/math.sin(2*a)))
print(round(v0,2))