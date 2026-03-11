from math import *

x= eval(input("Digite o valor do angulo x:"))
k= int(input("Digite o valor de k:"))

i= 0
soma= 0

while (i < k):
	soma= soma + (((-1) ** i) * (x ** (2 * i) / factorial(2 * i)))
	i= i + 1
	
print(round(soma, 10))