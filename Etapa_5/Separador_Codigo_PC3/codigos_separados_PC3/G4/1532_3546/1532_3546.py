from math import *

x = float(input())
k = float(input())
i = 0
senh = 0
t = 1
while (i < k):
	senh = senh + (x**t)/factorial(t)
	t = t + 2
	i = i + 1
print(round(senh, 9))
