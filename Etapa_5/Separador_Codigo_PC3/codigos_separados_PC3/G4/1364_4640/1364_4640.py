import math 
vel = float(input("velocity: "))
dist = float (input("distancia: "))
g = (9.8)
div = (90/math.pi)
gzin = (g / (vel**2))
ota = (dist * gzin)
alpha = math.asin(ota) * div 
print(round(alpha,2))