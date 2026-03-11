from math import*

x = float(input("digite um numero real:"))
k = int(input("digite um numero inteiro:"))
i = 0
soma= 0
sinal = 1
while (i < k): 
	soma = soma + (x ** i)* sinal 
	i = i + 1
	sinal = -sinal
print(round (soma, 7))