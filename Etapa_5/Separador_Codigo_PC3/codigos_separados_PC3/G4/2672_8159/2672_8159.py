import math
r=float(input("raio: "))
n=int(input("lados: "))
a = 1/2*(((r*(math.cos(math.pi/n))))**2)*math.tan(math.pi/n)
print(round(a,2))