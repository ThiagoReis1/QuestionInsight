a=float(input())
d=float(input())
g=9.8
from math import*
v=sqrt(d*(g/sin(2*radians(a))))
print(round(v,2))