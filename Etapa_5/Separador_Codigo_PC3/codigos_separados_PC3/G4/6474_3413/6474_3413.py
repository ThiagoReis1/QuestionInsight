import math
from math import *

def apotema(lado):
	return lado/(2 * math.tan(math.pi/11))

def area_undecagono(lado):
	a = apotema(lado)
	return 11 * lado * a / 2

lado = float(input())

area_total = area_undecagono(lado)

print(round(area_total,2))