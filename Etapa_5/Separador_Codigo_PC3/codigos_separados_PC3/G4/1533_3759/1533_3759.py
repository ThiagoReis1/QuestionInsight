x = int(input("Informe aqui o numero 1:"))
k = int(input("Informe aqui o numero 2:"))
from math import*
soma = 0
i = 0

while (i < k and k > 0):
	soma = soma + (x**(2*i))/(factorial(2*i))
	i = i + 1
print(round(soma,8))