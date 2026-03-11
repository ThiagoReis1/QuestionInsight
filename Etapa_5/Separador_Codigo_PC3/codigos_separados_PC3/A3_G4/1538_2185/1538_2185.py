from math import *
x = float(input("x: "))
n = int(input("k: "))
to = 1
t = 1
p = 1

while(p < n ):
	to = to + (x**(2*p)) * (-1)**p
	p = p+1

print(round(to,8))