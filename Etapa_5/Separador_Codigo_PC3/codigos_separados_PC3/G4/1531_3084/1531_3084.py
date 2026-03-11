from math import *
x = eval(input())
k = float(input())
i = 0
soma = 0 
while(i < k):
	soma = soma + (x ** i * (-1) ** i)/factorial(2**i)
	i = i + 1
print(round(soma, 10))