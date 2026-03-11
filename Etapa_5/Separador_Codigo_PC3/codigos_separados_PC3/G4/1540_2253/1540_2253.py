from math import*
b = eval(input(" "))
n = float(input(" "))
t = 0
a = 0
sinal = +1
while (t<n):
	a = a + (sinal * (b**(t)))/factorial(2*t)
	t = t + 1
	sinal = - sinal 
print(round(a,6))