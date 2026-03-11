from math import *
x = eval(input("x: "))
n = int(input("n: "))
x = radians(x)
a = 2
b = 2
while (n == 10):
	if (n%2 == 0):
		z = 1 - (x ** a/factorial(b))
		print(round(z,10))
	elif(n%2 != 0):
		z = 1 + (x ** a/factorial(b))
		print(round(z,10))
	a = a + 2
	b = b + 2
		