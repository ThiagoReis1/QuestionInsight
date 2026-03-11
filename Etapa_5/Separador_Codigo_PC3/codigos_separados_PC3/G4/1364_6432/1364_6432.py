from math import*

vo = float(input(""))
d = float(input(""))

g = 9.8

pr = asin(d*(g/(vo**2)))
sg = 90/pi

a = pr * sg 

print(round(a,2))


