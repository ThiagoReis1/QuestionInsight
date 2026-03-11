from math import *

angulo= float(input())
vel_inicial= float(input())

g= 9.8


d=((vel_inicial)**2 * sin(2 * radians(angulo)))/g

print(round(d,2))
