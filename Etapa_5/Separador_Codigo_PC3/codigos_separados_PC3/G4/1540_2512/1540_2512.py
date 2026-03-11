from math import *

x = eval(input())
k = int(input())

soma = 0
c = 0
f = 0
e = 0
a = 1

while(c<k):
	soma = soma + ((x**e)/(factorial(f)))*a
	c = c + 1
	f = f + 2
	e = e + 1
	a = a * (-1)
print(round(soma,6))
	