import math
r= float(input("raio"))
n = float(input("numero de lados"))
l = 2*r*math.sin(math.pi/n)
print(round(l,2))