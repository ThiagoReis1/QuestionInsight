r=float(input("raio: "))
n=int(input("lados: "))

import math

A=(1/2)*((r*math.cos(math.pi/n))**2*math.tan(math.pi/n))

print(round(A,2))