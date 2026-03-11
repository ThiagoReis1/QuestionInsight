from math import*
vinicial=float(input())
d=float(input())
g=9.8
ang=asin((d*g/vinicial**2))*(90/pi)
print(round(ang, 2))