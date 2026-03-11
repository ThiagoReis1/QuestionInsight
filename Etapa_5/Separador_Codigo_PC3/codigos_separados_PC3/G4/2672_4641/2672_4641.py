from math import*

r = float(input("quanto vale o raio?"))
n = int(input("quantos lados tem?"))

a = 1/2*((r*cos(pi/n))**2*tan(pi/n))

print(round(a,2))