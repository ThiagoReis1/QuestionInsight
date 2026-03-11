from math import*

r = float(input("raio:"))
l = int(input("lados:"))
p = pi

a = 1/2 *((r * cos(p/l))**2 * tan(p/l))

print (round(a, 2))