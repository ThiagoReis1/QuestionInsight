from math import *
x = float(input("Num. Real: "))
k = int(input("Num. Inteiro: "))

s = 0
i = 0
f = k-1
while(i<=f):
	s = s + (x**i)/factorial(i)
	i = i + 1
print(round(s,9))