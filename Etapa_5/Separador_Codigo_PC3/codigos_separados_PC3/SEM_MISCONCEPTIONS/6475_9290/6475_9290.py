from math import tan 
from math import pi

lado = int(input("lado"))

apotema = lado / (2 * tan(pi / 12))
a = 6 * lado * apotema

print(round(a,2))