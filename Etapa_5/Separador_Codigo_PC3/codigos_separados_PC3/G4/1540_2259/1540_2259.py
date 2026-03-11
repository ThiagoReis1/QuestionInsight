from math import *
ang = eval (input("digite:"))
k = eval(input("digite o valor de k:"))
soma = 0
i = 0 
sinal = 1

while (i<k):
	soma = soma + sinal * (ang**(2 * i +1)/factorial(2 * i +1))
	i = i + 1
	sinal = - sinal
print(round(soma,6))	