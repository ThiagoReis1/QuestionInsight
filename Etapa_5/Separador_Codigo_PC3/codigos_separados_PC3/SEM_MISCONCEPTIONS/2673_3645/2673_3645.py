import math
raio = float(input())
lados = int(input())
l = 2 * raio * math.sin(math.pi/lados)
print(round(l,2))