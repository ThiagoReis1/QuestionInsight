from math import*

x = eval(input("digite o valor: "))
k = int(input("informe outro valor: "))

sinal = +1
i = 0
soma = 0
while(i < k):
	sinal = - sinal
	i = i + 1
	soma = soma + sinal * (x**(i)) / factorial(i)
	
print(round(soma , 10))