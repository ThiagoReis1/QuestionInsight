from math import *

ang= float(input())
vel= float(input())
g= 9.8
ang1= radians(ang)
d=vel**2*sin(2*ang1)/g

print(round(d,2))