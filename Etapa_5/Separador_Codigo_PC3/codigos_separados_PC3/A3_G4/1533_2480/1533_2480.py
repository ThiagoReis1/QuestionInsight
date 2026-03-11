from math import*
x = float(input("Valor : "))
k = int(input("Valor : "))

soma = 1
t=0

while (t < k):
	soma = 1 + (x**(2*t))/(factorial(2*t))
	t = t + 1

	print (round(soma, 8))