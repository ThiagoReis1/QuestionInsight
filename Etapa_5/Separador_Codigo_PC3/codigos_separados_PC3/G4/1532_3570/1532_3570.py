from math import *
n = int(input("digite um valor:"))
k = int(input("quantidade de termos:"))

i = 0
soma = 0

while(i < k):
	sen = (n**(1 + 2*i))/factorial(1 + 2*i)
	soma = soma + sen
	i = i + 1
	
print(round(soma,9))	