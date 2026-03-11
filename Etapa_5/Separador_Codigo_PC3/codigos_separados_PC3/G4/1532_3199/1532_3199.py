from math import *
x = float(input("x: "))
k = int(input("k: "))
s = 0
n = 1
while (n<k):
	s = s + ((x**n) / factorial (n))
	n = n + 2
	print(s)