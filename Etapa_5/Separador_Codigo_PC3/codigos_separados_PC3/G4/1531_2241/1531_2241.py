from math import *
x= eval(input())
k=int(input())
d = 1
a = 2
sinal = -1
cx = 0
while(d < k):
	cx = cx + (sinal)*((x**a)/(factorial(a)))
	sinal= -sinal
	a = a + 2
	d = d + 1
print(round(cx + 1,10))