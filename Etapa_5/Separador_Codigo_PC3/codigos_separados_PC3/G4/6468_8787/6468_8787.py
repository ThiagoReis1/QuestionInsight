from math import pi
from math import tan 
l = float(input("digite lado: "))
apo = l / (2 * tan (pi/5))
ap = (5 * l * apo) / 2 
print(round(ap, 2))