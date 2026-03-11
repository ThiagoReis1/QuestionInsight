from math import*

x = int(input("digite um numero: "))
k = int(input("digite um numero: "))

soma = 0
sinal = -1
e = 1
a = 1
while (e <= k):
	soma = soma - sinal * (x**e/a)
	sinal = -sinal
	e = e+4
	a = a+2
print(round(soma ,6))
