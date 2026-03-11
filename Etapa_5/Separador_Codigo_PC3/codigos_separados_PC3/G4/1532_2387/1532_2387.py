from math import*
x = float(input())
k = int(input())

y = x
exp = 3
i = 1
while(i < k):
	y = y +((x**exp)/factorial(exp))
	exp = exp + 2
	i = i + 1

print(round(y,9))	