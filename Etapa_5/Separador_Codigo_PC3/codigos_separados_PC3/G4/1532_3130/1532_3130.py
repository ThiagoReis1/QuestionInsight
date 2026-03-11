from math import*
x = float(input(""))
k = int(input(""))
a = 0
b = 0
c = 1
while(b < k):
	a = a + x**(c) / factorial(c)
	c = c + 2
	b = b + 1
print(round(a,9))