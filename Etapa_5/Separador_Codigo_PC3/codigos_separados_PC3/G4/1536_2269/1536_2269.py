from math import*
x = float(input(": "))
k = int(input(": "))
i = 0
a = 0
t = 2
sinal = + 1
while(i < k):
	a = a + (1 - x**2)+(x**3)-(x**4)+(x**5)/factorial(t)
	i = i + 1
	t = t + 2
	sinal = - sinal
print(round(a,10))
	
	
	
	
