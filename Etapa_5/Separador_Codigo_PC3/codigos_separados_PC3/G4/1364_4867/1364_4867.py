from math import*
v=float(input("v="))
d=float(input("d="))
a=asin(d*(9.8/(v**2)))*(90/pi)
print(round(a,2))