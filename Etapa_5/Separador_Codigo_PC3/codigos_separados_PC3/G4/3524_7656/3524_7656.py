from math import*
x = float(input("Informe um numero real: "))
k = int(input("Informe um numero inteiro: "))
c = 0
c1 = 0
soma = 0

while(c1<k):
	soma += (x**c)/(factorial(c))
	c += 2
	c1 += 1
	
print(round(soma,8))