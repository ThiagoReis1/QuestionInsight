from math import *
x = float(input("Digite: "))
k = int(input("digite: "))
e = 0
den = 0
i = 0
while(i < k):
	e = e + (x**den) / factorial(den)
	den = den + 2
	i = i + 1
print(round(e, 8))