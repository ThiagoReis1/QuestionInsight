from math import*
a=float(input("angulo:"))
v=float(input("vel:"))
g=9.8
d=(v**2)*sin(radians(2*a))/g
print(round(d,2))