from math import *

ladoB = float(input())
ladoC = float(input())
alpha = radians(float(input()))
ladoA = sqrt(ladoB**2 + ladoC**2 - 2*ladoB*ladoC*cos(alpha))
print(round(ladoA, 2))