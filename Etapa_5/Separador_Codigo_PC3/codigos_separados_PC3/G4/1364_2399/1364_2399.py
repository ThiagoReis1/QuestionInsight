from math import*
v1 = float(input())
d1 = float(input()) 
g = 9.8

a = asin( d1 * g / v1 ** 2) * 90 / pi



print(round(a,2))