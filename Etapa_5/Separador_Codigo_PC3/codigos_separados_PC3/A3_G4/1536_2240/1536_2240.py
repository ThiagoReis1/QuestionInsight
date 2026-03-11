from math import*
x = float(input())
k = int(input())
t = 1
q = 0
j = 0
a = 1
sinal = 1
while(t <= k):
	j = ((j + sinal*((x**a)/a)))
	t = t + 1
	a = a + 1
	sinal = (-sinal)
print(round(j,10))













































