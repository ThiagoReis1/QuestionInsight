from math import *
x = eval(input())
k = int(input())
i = 1
a = 2
sinal = -1
cx = 0
while(i < k):
	cx += sinal*((x**a)/(factorial(a)))
	sinal = - sinal
	a = a + 2
	i = i + 1
print(round(cx + 1, 10))