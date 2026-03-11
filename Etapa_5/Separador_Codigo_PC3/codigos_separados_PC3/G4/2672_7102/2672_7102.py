from math import *

raio = float(input())
n = float(input())

a = 1/2 * ( ((raio * (cos(pi/n)))** 2) * tan(pi/n))

print(round(a,2))