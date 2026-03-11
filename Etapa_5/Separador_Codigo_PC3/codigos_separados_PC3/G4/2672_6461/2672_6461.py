from math import *

r = float(input("raio de r: "))
n = int(input("lados de n: "))

x = r * cos(pi / n) 
y = tan(pi / n)

a = 1 / 2 * ((x) **2) * y

print(round(a, 2))