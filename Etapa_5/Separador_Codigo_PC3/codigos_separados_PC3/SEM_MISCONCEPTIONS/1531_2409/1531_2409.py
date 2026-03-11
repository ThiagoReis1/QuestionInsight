from math import *
x = eval(input("digite o angulo: "))
k = int(input("digite o numero de series: "))

i = 1
soma = 1.0

sinal = -1

while(i < k):
	termo = sinal * x**(2*i) / factorial(2*i)
	soma = soma + termo 
	i = i + 1
	sinal = - sinal 
print(round(soma, 10))