from math import *
x = eval(input(""))
k = int(input(""))
exp = 0
fac = 2
soma = 0
sinal = 1
i = 0
while (i < k):
	soma = soma + sinal * (x**(exp)) / (factorial(2*exp))
	sinal = sinal * (-1)
	i = i + 1
	exp = exp + 1
print(round(soma, 6))