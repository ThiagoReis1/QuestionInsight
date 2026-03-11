from math import*

ang = eval(input("var1: "))
k = int(input("var2: "))
soma = 0
i = 0

while(i < k):
	soma = soma + ((-1) ** i) * (ang ** (2*i) / factorial(2*i))  
	i = i + 1

print(round(soma, 10))