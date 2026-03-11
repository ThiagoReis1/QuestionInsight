from math import*
r = float(input())
n = int(input())
A = 0.5*(r*cos(pi/n))**2 * tan(pi/n)
print(round(A,2))