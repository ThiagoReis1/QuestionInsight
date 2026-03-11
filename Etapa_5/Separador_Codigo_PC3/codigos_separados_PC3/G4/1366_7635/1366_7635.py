from math import*

a = float(input("angulo da flecha:"))
b = float(input("volocidade da flecha:"))
g = 9.8

d = b**2*(sin(2 * radians(a))/g)

print(round(d, 2))