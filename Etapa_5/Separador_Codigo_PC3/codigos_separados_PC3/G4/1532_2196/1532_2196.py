from math import*
x = float(input("digite valor de x: "))
k = int(input("digite o valor de k: "))

a = 0
e = k
while(a < x):
	e = e +(a**1/factorial(a))
	a = a + 1
print(e)