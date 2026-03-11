import math
sin = math.sin
radians = math.radians
x = float(input("qual o angulo? "))
y = float(input("qual a veloc? "))
dist = y**2*sin(radians(2*x))/9.8


print(round(dist,2))