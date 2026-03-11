from math import *

bm = float(input())
bme = float(input())
h = float(input()) 
custo = float(input())

area = h * (bm + bme) 
area1 = area / 2
custo1 = (custo*area1)

print(round(custo1, 2))


