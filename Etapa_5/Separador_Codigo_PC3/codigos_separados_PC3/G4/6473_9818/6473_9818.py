from math import *

lado = float(input())
apot = lado / (2 * tan(pi/10))
adec = 5 * lado * apot

print(round(adec, 2))
