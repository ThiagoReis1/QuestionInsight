from math import *

num =float(input("numero real:"))
qt = int(input("quantidade de termos:"))
i = 0
soma = 0
while(i < qt):
	soma =soma + num**(2*i+1)/(factorial(2 * i + 1))
	i = i + 1

print(round(soma,9))