import math

raio = float(input())
lado = int(input())

res = raio * math.cos(math.pi/lado)
print(round(res,2))