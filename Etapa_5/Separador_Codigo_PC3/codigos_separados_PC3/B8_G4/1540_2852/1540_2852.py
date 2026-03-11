from math import*
x = eval(input(" angulo x "))
k = int(input(" quantidade de termos "))
a = 1
b = 1
c = 1
n = 2
while (k > a):
	if (c%2 != 0):
		b = b - (x**c)/factorial(n)
	elif (c%2 == 0):
		b = b + (x**c)/factorial(n)
	a = a + 1
	c = c + 1
	n = n + 2
print(round(b,6))