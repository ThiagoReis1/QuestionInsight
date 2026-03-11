import math

lado = float(input())

apotema = lado/(2*math.tan(math.pi/6))

area = 3 * lado * apotema

print(round(area,2))