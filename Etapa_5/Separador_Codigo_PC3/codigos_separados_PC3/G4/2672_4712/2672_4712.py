import math
r = float(input())
n = int(input())
a = (1/2)*((r*math.cos(math.pi/n))**2 * math.tan(math.pi/n))
print (round(a,2))