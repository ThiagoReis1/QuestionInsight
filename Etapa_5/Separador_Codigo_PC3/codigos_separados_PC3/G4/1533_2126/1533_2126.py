from math import*
x = float(input("Um número real:"))
k = int(input("Um número inteiro, a quantidade de termos da série:"))
soma = 0
i = 0
while(i<k):
	soma = soma + (x**(i*2)/(factorial(i*2)))
	i = i + 1
print (round(soma,8))