from math import*

x = float(input())
k = int(input())

i = 0
c = 0
h = 0

while (i < k):
	h = h + (x ** c) / (factorial(c))
	c = c + 1
	i = i + 1
print(round(h,9))