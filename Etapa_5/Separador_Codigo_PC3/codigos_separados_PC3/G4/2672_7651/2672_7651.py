import math
raio = float(input())
n = int(input())

area = (1/2) * ((raio * (math.cos(math.pi/n)))**2 * math.tan(math.pi/n))

print(round(area, 2))