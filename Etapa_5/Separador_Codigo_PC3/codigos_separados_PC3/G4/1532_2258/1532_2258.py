from math import*
x = float(input(":"))
k = int(input(":"))
a = 3
s = x
i = 1
while (i<k):
	s = s + x**a/factorial(a)
	a = a + 2
	i = i + 1
print(round(s,9))