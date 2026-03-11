from math import *
a= radians(float(input()))
d= float(input())
v = sqrt((d*(9.8))/(sin(2*a)))
print (round(v,2))