#Dina Karen Barros 
#Trabalho Prático 04
#ex 02

from math import*

x = eval(input("Digite o ânulo:"))
k = int(input("Digite a qtdade de termos:"))

soma = 1
d = 2
i = 1

#laço

while (i < k):
	soma = soma + (-1)**i * (x**(d)/factorial(d))
	i = i + 1
	d = d + 2
	
print(round(soma,10))