from math import*
x = eval(input(": "))
k = int(input(": "))
serie = 1
sinal = -1
a = 2
while(a < k):
	serie = serie + (sinal) * (x**a/ factorial(a))
	sinal = sinal * -1
   a = a + 2
print(round(serie,10))