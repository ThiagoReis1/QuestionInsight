from math import *
x = eval(input("angulo: "))
k = int(input("termos: "))
i = 0
soma = 0
while(i<k):
	soma = soma + (-1)**i * (x**(i))/factorial(2*i)
	i = i + 1
print(round(soma, 6))