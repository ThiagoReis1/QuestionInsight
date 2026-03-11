from math import*
x = float(input())
k = float(input())
i = 0
n = 0
c = 0
while(n<(k)):
	c = c + (x**i/factorial(i))
	i = i + 1
	n = n + 1
	e = c
print(round(e, 9))