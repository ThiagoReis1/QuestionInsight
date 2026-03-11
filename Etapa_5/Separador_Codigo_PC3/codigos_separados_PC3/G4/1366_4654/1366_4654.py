import math 
angulo = math.radians (float(input()))
vi = float(input())
g = 9.8
d = vi**2 * math.sin(2*angulo)/g

print(round(d,2))