from math import *

x = eval(input("valor do angulo: "))
k = int(input("quantidade de termos: "))

i = 1
a = 2
sinal = -1
eq = 1.0

while(i < k):
	eq = sinal * (x ** i)/factorial(a) + eq
	i = i + 1
	a = a + 2
	sinal = -sinal
	
print(round(eq, 6))
	