from math import *
x = eval(input('x: '))
k = int(input('k: '))
i = 1
soma = 0
sinal = +1
while i <= k - 1:
	soma = soma + sinal * (x ** (2*i) / factorial(2*i))
	i = i + 2
	sinal = -sinal
result = soma
print(round(result, 10))

