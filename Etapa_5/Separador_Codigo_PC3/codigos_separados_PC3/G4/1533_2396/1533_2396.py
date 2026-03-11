from math import*
x0 = float(input())
k = int(input())
y = 2
x = 1
i = 1
while(i<k):
	x = x + (x0**y)/factorial(y)
	y = y+2
	i = i+1
print(round(x, 8 ))