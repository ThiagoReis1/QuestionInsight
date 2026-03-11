import math

b = float(input())
c = float(input())
ang = math.radians(float(input()))

calculo = math.sqrt(b**2 + c**2 - 2*b*c*math.cos(ang))

print(round(calculo,2))
