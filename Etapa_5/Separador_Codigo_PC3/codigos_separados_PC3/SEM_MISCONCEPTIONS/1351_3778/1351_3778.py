import math

est = float(input())
aresta = float(input())

area = 3 * (math.sqrt(3 * aresta ** 2)) / 2
print(int(area * est))