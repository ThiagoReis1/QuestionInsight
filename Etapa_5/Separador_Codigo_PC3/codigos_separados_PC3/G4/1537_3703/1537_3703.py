from math import*
x = float(input())
k = int(input())
k0 = 0
e = 0
while k0 < k:
	e = e + (x**k0/factorial(k0))
	k0 = k0 +1
print(round(e,9))