from math import *

CL = float(input("digite o comprimento do lado do undecagono:"))

D = 2* tan(pi/11)
apotema = (CL/D)
AU = (11* CL * apotema/2)

print(round(AU,2))