import math

b = float(input())
c = float(input())
alfa = math.radians(float(input()))

a = math.sqrt(math.pow(b,2)+math.pow(c,2)-(2*b*c*math.cos(alfa)))

print(round(a,2))