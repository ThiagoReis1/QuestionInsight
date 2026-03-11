from math import *

r=float(input(""))
n=int(input(""))

area = 1/2 * ( r * cos(pi/n))**2  * tan(pi/n)

print(round(area,2))