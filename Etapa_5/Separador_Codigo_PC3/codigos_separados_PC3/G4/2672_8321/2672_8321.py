from math import *

r = float( input("raio"))
n = int( input("numero de lados"))

a = 0.5*((r*cos(pi/n))**2 *tan(pi/n))

print(round(a,2))