from math import *
v = float(input("vel:"))
d = float(input("dist:"))
ang = asin(d*9.8/v**2)*90/pi

print(round(ang,2))

