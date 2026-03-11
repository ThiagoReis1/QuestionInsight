r = float(input("Raio.  "))
n = int(input("Numero de lados.  "))
from math import *

a = r * cos(pi/n)

print(round(a,2))