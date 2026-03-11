from math import*

soma = 1
i = 1


x = eval(input("Insira um angulo: "))
k = int(input("Insira um numero: "))

while(i < k):
	soma = soma + ((x**(2*i))/factorial(2*i))*((-1)**i*1)
	i = i + 1

	
print(round(soma,10)) 