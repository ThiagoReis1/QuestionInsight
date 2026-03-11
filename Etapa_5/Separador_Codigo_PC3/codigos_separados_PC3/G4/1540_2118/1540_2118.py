from math import*

x = eval(input(""))
k = int(input(""))
i = 0
t = 1
sinal = 1

while(i<k):
	sinal = -sinal
	c = 1 + (x**i*sinal)/factorial(t)
	i = i+1
	t = t+1
	
print(round(c,6))
	
