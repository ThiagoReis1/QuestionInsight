from math import*
r = float(input("raio:"))
n = int(input("lado:"))
L = 2*r*sin(pi/n)
print(round(L, 2))