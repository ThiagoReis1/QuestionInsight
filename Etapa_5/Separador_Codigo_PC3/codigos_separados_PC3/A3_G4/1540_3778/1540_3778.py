import math
pi = math.pi
x = eval(input())
k = int(input())
r = 1
i = 1
a = 2
while i < k:
	if i%2 == 0:
		r = r + (x**i/math.factorial(a))
	else:
		r = r - (x**i/math.factorial(a))
	i = i + 1
	a = a + 2
print(round(r, 6))