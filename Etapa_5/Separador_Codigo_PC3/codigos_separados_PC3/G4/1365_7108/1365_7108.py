from math import*

a= radians(float(input()))
d= float(input())

vo= d*(9.8/sin(2*a))
r= sqrt(vo)

print(round(r,2))