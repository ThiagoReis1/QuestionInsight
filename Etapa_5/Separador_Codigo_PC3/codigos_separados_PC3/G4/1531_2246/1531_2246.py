from math import*
b = eval(input(":"))
n= int(input(":"))
t= 0
a= 0
sinal = +1
while(t<n):
	a = a + (sinal) * (b**(2*t))/ factorial(2*t)
	t = t + 1
	sinal= - sinal
print(round(a,10))