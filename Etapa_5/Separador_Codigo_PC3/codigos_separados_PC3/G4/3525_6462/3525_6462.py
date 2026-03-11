from math import *
x = float(input())
k = int(input())
soma = 0
i = 0
while (i< k):
	soma = soma + x**(2*i+1)/(factorial(2*i+1))
	i = i+1
print(round(soma , 9))