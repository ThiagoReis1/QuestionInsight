from math import * 

r, n = float(input()), int(input())

area = 0.5*((r*cos(pi/n))**2*tan(pi/n))

print(round(area, 2))