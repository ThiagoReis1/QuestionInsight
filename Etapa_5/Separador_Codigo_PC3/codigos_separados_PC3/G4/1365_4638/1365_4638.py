ang = float(input("qual o angulo ?"))

dist = float(input("qual a distancia ?"))

from math import * 

v0 = sqrt(dist*9.8/sin(2*radians(ang)))

print(round(v0, 2))