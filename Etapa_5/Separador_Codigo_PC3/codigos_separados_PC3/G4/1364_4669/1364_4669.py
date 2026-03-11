from math import*
v = float(input())
d = float(input())
ang = asin(d*(9.8/v**2))*(90/pi)
print(round(ang, 2))