from math import*
x = eval(input("insira ang: "))
k = int(input("insira o termo: "))
i = 0
soma = 0
while(i<k):
	soma = soma + (-1)**i * (x**(2*i))/factorial(2*i)
	i = i+1
print(round(soma,10))
