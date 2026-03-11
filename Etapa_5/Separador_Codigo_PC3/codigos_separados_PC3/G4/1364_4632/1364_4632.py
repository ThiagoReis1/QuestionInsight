import math
v = float(input())
d = float(input()) 
g = 9.8
n1 = (d) * (g/(v)**2)
n2 = 90/math.pi
n3 = math.asin(n1)
alpha = n3 * n2
print(round(alpha,2))
