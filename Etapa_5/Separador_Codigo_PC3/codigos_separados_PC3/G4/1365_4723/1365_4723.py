from math import *
a= float(input())
d= float(input())
g= 9.8
a = radians(a)
vo= sqrt(d*(g/sin(2*a)))
print(round(vo,2))