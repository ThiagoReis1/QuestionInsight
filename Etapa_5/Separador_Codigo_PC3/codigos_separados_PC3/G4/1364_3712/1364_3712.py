from math  import *

v0 =  float(input("v0"))
d = float(input("distancia"))
g= 9.8
v1 = d*g
v2= v1/v0**2
ang = asin(v2)*90/pi

print(round(ang,2))