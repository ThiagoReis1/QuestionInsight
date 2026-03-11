from math import*

ang = radians (float (input()))
d = float (input())

v0 = sqrt (d * 9.8/sin(2*ang))

print (round (v0, 2))